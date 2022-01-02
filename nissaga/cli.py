#!/usr/bin/env python3

from nissaga.models import Nissaga, schema_json, schema_yaml
from nissaga.render import render
from yamlns import namespace as ns
from consolemsg import step, error
import graphviz
from pathlib import Path
import typer
from typing import List, Union, Optional
from enum import Enum

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
    name='nissaga',
    help="Nissaga is a genealogy tree generator",
    no_args_is_help = False,
)

@app.command()
def draw(
    yamlfile: Path = typer.Argument(...,
        help = "Input yaml file to process",
        exists=True,
        dir_okay=False,
        readable=True,
        allow_dash=True,
    ),
    format: Optional[List[OutputFormat]] = typer.Argument(None,
        help = "Output formats, pdf if not specified",
    ),
):
    "Draws the tree for the input file"

    data = ns.load(yamlfile)
    formats = [f.value for f in format] or ['pdf']

    step("Validating...")
    p=Nissaga(**data)

    step("Normalizing...")
    p.normalize()

    dotfile = yamlfile.with_suffix('.dot')

    step("Generating graph...")
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


@app.command("schema")
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

def main():
    app()
