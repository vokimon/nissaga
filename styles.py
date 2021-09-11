from yamlns import namespace as ns

default_styles = ns.loads("""
  ':edge':
    dir: 'none'
    color: '#cccccc'

  ':house':
    style: 'filled'
    color: '#fafafa'
    labeljust: 'l'
    fontname: 'Helvetica, Arial, sans-serif'
    fontsize: 16
    margin: 10

  ':house-2':
    color: '#ffffff'

  # Family subgraph
  ':family':
    label: ''
    style: 'invis'
    margin: 0

  ':node':
    shape: 'box'
    style: 'filled'
    fontname: 'Helvetica, Arial, sans-serif'
    width: 2.5
    fillcolor: 'white'
    color: '#cccccc'

  ':digraph':
    rankdir: 'LR'
    ranksep: 0.4
    splines: 'ortho'

  ':union':
    shape: 'circle'
    style: 'filled'
    penwidth: 1
    color: 'white'
    label: ''
    height: 0.1
    width: 0.1
    fontname: 'Helvetica, Arial, sans-serif'
    fontsize: 9
    fontcolor: '#660000'

  ':children':
    shape: 'box'
    style: 'filled'
    label: ''
    height: 0.005 # Make it look like a line. Brilliant!
    penwidth: 0
    width: 0.1

  ':parent-link':
    weight: 2 # give priority to be straighter than parent2

  ':parent2-link':
    style: 'dashed'
    penwidth: 0.25
    weight: 1

  ':parent-child-link':
    weight: 3 # prefer bridges to be straight

  ':child-link':
    dir: 'forward'
    arrowhead: 'tee'
    arrowsize: 2
    weight: 2

  ':child2-link':
    style: 'dashed'
    penwidth: 0.25
    weight: 1
""")


def escape(s):
    # TODO: review this
    if type(s)==str:
        return '"'+s+'"'
    return s

def renderStyle(styles):
    return [
        f"{name}={escape(value)}"
        for name, value in styles.items()
        if value is not None
    ]

def combineStyles(tree, *classes, pre={}, post={}, **additional):
    result = ns(pre)
    for clss in classes:
        result.update(default_styles.get(clss, {}))
        result.update((tree.styles or {}).get(clss, {}))
    result.update(post)
    return result

def applyStyles(tree, *classes, pre={}, post={}, **additional):
    return renderStyle(
        combineStyles(tree, *classes, pre=pre, post=post, **additional)
    )

