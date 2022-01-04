#!/usr/bin/env python3

from yamlns import namespace as ns
from consolemsg import step, error
import graphviz
from pathlib import Path
import typer
from typing import List, Union, Optional
from enum import Enum
from .models import Nissaga, schema_json, schema_yaml
from .render import render
from . import __version__

class SchemaFormat(str, Enum):
    json = 'json'
    yaml = 'yaml'

class OutputFormat(str, Enum):
    pdf = 'pdf'
    svg = 'svg'
    png = 'png'
    dot = 'dot'
    jpg = 'jpg'

app = typer.Typer(
    no_args_is_help = False,
)

def version_callback(value: bool):
    if not value: return
    typer.echo(f"Nissaga {__version__}")
    raise typer.Exit()

def backend_callback(value: bool):
    if not value: return
    typer.echo(f"Using GraphViz {'.'.join(str(x) for x in graphviz.version())}")
    typer.echo(f"Supported output formats: {', '.join(graphviz.FORMATS)}")
    raise typer.Exit()

@app.callback()
def nissaga(
    version: Optional[bool] = typer.Option(
        None, "--version",
        callback=version_callback,
        is_eager=True,
        help="Show the version and exit.",
    ),
    backend: Optional[bool] = typer.Option(
        None, "--backend",
        callback=backend_callback,
        is_eager=True,
        help="Show GraphViz backend information and exit.",
    ),
):
    "Nissaga is a genealogy tree generator"

@app.command()
def draw(
    yamlfile: Path = typer.Argument(...,
        help = "Input yaml file to process",
        exists=True,
        dir_okay=False,
        readable=True,
        #allow_dash=True,
    ),
    format: Optional[List[OutputFormat]] = typer.Argument(None,
        help = "Output formats, pdf if not specified",
    ),
):
    "Draws the tree for the input file"

    formats = [f.value for f in format] or ['pdf']

    step(f"Loading {yamlfile}...")
    p = Nissaga.load(yamlfile)

    dotfile = yamlfile.with_suffix('.dot')

    dot = render(p)
    Path(dotfile).write_text(dot, encoding='utf8')

    gv = graphviz.Source(dot)
    for format in formats:
        if format == 'dot': continue
        outputfile = yamlfile.with_suffix('.'+format)
        step("Generating {}...", outputfile)
        try:
            temp = gv.render(dotfile, format=format, view=False)
            Path(temp).rename(outputfile)
        except graphviz.backend.CalledProcessError as exception:
            print(dir(exception))
            error(exception.stderr)
            error("Intermediate dot file dumped as output.dot")

    if 'dot' not in formats:
        dotfile.unlink()
    else:
        step("Generating {}...", dotfile)


@app.command()
def schema(
    format: SchemaFormat = typer.Argument('yaml',
        help= "Format",
    ),
):
    "Dumps the schema for the input files"
    if format == 'json':
        step("Generating 'nissaga-schema.json'")
        Path('nissaga-schema.json').write_text(schema_json(), encoding='utf8')
    elif format == 'yaml':
        step("Generating 'nissaga-schema.yaml'")
        Path('nissaga-schema.yaml').write_text(schema_yaml(), encoding='utf8')

