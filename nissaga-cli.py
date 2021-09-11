from nissaga.models import KinFile
from nissaga.render import render
from yamlns import namespace as ns
from consolemsg import step
import graphviz
from pathlib import Path

if __name__ == '__main__':
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

    step("Generating pdf...")
    graphviz.Source(dot).render('output.pdf', format='pdf', view=True)


