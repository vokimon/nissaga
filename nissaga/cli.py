#!/usr/bin/env python3

from nissaga.models import Nissaga, schema_json, schema_yaml
from nissaga.render import render
from yamlns import namespace as ns
from consolemsg import step, error
import graphviz
from pathlib import Path

supportedFormats = 'pdf svg png jpg'

def main():
    import sys

    if 'schema' in sys.argv:
        formats = [a for a in sys.argv if a in ('json', 'yaml')] or ['yaml']
        if 'json' in formats:
            Path('nissaga-schema.json').write_text(schema_json(), encoding='utf8')
        if 'yaml' in formats:
            Path('nissaga-schema.yaml').write_text(schema_yaml(), encoding='utf8')
        sys.exit(0)

    inputfile = Path(sys.argv[1])
    formats = [f for f in sys.argv[2:]] or ['pdf']

    step("Loading {}...", inputfile)
    data = ns.load(inputfile)

    step("Validating...")
    p=Nissaga(**data)

    step("Normalizing...")
    p.normalize()

    #print(ns(p.dict()).dump())

    dotfile = inputfile.with_suffix('.dot')

    step("Generating graph...")
    dot = render(p)
    Path(dotfile).write_text(dot, encoding='utf8')

    gv = graphviz.Source(dot)
    for format in formats:
        if format == 'dot': continue
        outputfile = inputfile.with_suffix('.'+format)
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


