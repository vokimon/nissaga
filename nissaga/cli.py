#!/usr/bin/env python3

from nissaga.models import KinFile, schema
from nissaga.render import render
from yamlns import namespace as ns
from consolemsg import step
import graphviz
from pathlib import Path

def main():
    import sys

    inputfile = Path(sys.argv[1])
    format='pdf'
    if len(sys.argv)>2:
        format=sys.argv[2]
    outputfile = inputfile.with_suffix('.'+format)

    step("Loading {}...", inputfile)
    data = ns.load(inputfile)

    step("Validating...")
    p=KinFile(**data)

    step("Normalizing...")
    p.normalize()

    #print(ns(p.dict()).dump())

    step("Generating graph...")
    dot = render(p)
    Path('output.dot').write_text(dot, encoding='utf8')
    Path('nissaga-schema.json').write_text(schema(), encoding='utf8')
    Path('nissaga-schema.yaml').write_text(ns(KinFile.schema()).dump(), encoding='utf8')

    step("Generating {}...", outputfile)
    temp = graphviz.Source(dot).render('output', format=format, view=False)
    Path(temp).rename(outputfile)

