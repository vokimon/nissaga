#!/usr/bin/env python3

from nissaga.models import KinFile, schema
from nissaga.render import render
from yamlns import namespace as ns
from consolemsg import step
import graphviz
from pathlib import Path

def main():
    import sys

    step("Loading {}...", sys.argv[1])
    data = ns.load(sys.argv[1])

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

    step("Generating pdf...")
    graphviz.Source(dot).render('output', format='pdf', view=False)


