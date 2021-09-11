import graphviz
from pydantic import BaseModel, Extra, AnyHttpUrl
from yamlns import namespace as ns
from typing import Union, Optional, Dict, List 
import datetime
from consolemsg import warn
import sys
from pathlib import Path

familyColors=[
    '#1abc9c',
    '#2ecc71',
    '#3498db',
    '#9b59b6',
    '#34495e',
    '#f1c40f',
    '#e67e22',
    '#e74c3c',
]
styles = ns.loads("""
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


class Person(BaseModel):
    born: Optional[Union[bool, datetime.date, str]] = True
    died: Optional[Union[bool, datetime.date, str]] = False
    age: Optional[int]
    comment: Optional[Union[str,List[str]]]
    notes: Optional[str]
    alias: Optional[str]
    from_: Optional[str]
    todo: Optional[Union[str,List[str]]]
    pics: Optional[List[str]]
    docs: Optional[List[str]]
    links: Optional[List[str]] #Optional[List[AnyHttpUrl]]
    class_: Optional[List[str]]

    class Config:
        extra = Extra.forbid
        fields = dict(
            from_ = 'from',
            class_ = 'class',
        )

class Family(BaseModel):
    parents: List[Union[str, Dict[str, Person]]]
    children: Optional[List[Union[str, Dict[str, Person]]]]
    married: Optional[Union[bool, datetime.date, str]] = True
    divorced: Optional[Union[bool, datetime.date, str]] = False
    house: Optional[str]
    notes: Optional[str]
    docs: Optional[List[str]]
    families: Optional[List['Family']] = []

    class Config:
        extra = Extra.forbid

Family.update_forward_refs()
 
class KinFile(BaseModel):
    styles: Dict = None
    families: List[Family] = None
    people: Dict[str, Person] = None

    class Config:
        extra = Extra.forbid


def escape(s):
    # TODO: review this
    return '"'+s+'"'


def processPerson(person, people):
    if type(person) is str:
        if person not in people:
            people[person] = None
        return person

    for name, p in person.items():
        if people.get(name, None) is not None:
            warn(f"Person {name} specified twice")
        people[name] = p
        return name

def processFamily(data, people):
    if 'families' not in data: return
    for family in data.families:
        family.parents = [
            processPerson(parent, people)
            for parent in family.parents
        ]
        family.children = [
            processPerson(child, people)
            for child in family.get('children', [])
        ]
        processFamily(family, people)

def indenter(data, spacer='  '):
    def subindenter(data, level=-1):
        if type(data) == str:
            return [level*spacer + data]
        return sum((
            subindenter(element, level+1)
            for element in data
        ), [])

    return '\n'.join(subindenter(data))

def render(data):
    return indenter([
        'digraph G {', [
            'edge [', [
                'dir="none"',
                'color="#cccccc"',
                ],
            ']',
            '',
            'node [', [
                'shape="box"',
                'style="filled"',
                'fontname="Helvetica, Arial, sans-serif"',
                #'width=2.5',
                'width=3.2', # This one from my file
                'fillcolor="white"',
                'color="#cccccc"',
                ],
            ']',
            '',
            'rankdir="LR"',
            'ranksep=0.4',
            'splines="ortho"',
            '',
        ]+
        sum([
            renderFamily(data, data, f, [str(i)])
            for i,f in enumerate(data.get('families',[]))
        ] + [
            renderPerson(data, p or {}, [str(n)])
            for i,(n,p) in enumerate(data.get('people',ns()).items())
        ], []),
        '}'
    ])

def renderHousePrelude(family, path):
    if not family.get('house', None):
        return []
    return [
        '#'*76,
        f'# House {".".join(path)} - {family.house}',
        '#'*76,
        '',
        f'label=<<b>{family.house}</b>>',
        #f'labelhref="{family.links and family.links[0]}"',
        # style :house before: label:label labelhref=labelhref
        'style="filled"',
        'color="#fafafa"' if not len(path)&1 else 'color="#f4f4f4"',
        'labeljust="l"',
        'fontname="Helvetica, Arial, sans-serif"',
        'fontsize=16',
        'margin=10',
        '',
    ]


def renderFamily(data, house, family, path):
    family.color = familyColors[ int(path[-1]) % len(familyColors) ]
    slug='_'.join(str(p) for p in path)
    jointparents = ', '.join([p for p in family.parents if p]) or "none"
    jointchildren = ', '.join([p for p in family.children if p]) or "none"
    return [
        f'subgraph cluster_family_{slug} {{', [
            # TODO style :family
            'label=""',
            'style="invis"',
            'margin=0',
            '',
            ] +
            renderHousePrelude(family, path) +
            renderSubFamilies(data, family, path) +
            [
            f'# Family [{jointparents}] -> [{jointchildren}]', 
            '# ' + '-'*74,
            '',
            ] +
            renderParents(family, slug) +
            renderLink(family, slug) +
            (renderKids(family, slug) if family.children else ['# No children']) +
            #(renderKidLinks(family, slug) if len(family.children)>1 else []) +
            [
            ],
        '}',
        '',
    ]

def renderParents(family, id):
    if not family.parents:
        return ['# No parents']

    union = f'union_{id}'
    return [
        f'{union} [', [
            f'fillcolor="{family.color}"',
            # style :union fillcolor=color
            'shape="circle"',
            'style="filled"',
            'penwidth=1',
            'color="white"',
            'label=""',
            'height=0.1',
            'width=0.1',
            ],
        ']',
        '',
    ] + ([
        f'{{{", ".join([escape(p) for p in family.parents])}}} -> {union} [', [
            # TODO: style :parent-link color=color
            f'color="{family.color}"',
            'weight=2', # give priority to be straighter than parent2
        ], ']',
    ] if family.parents else [])

def renderLink(family, id):
    if not family.parents: return []
    if not family.children: return []

    return [
      f'union_{id} -> siblings_{id} [', [
          # TODO style :parent-link, :parent-child-link color=color
          f'color="{family.color}"',
          'weight=3',
      ], ']',
    ]

def renderKids(family, id):
    if not family.children:
        return ['# No children']

    kids = f'siblings_{id}'
    union = f'union_{id}'
    return [
        f'{kids} [', [
            f'fillcolor="{family.color}"',
            # TODO style :children fillcolor: color
            'shape="box"',
            'style="filled"',
            'label=""',
            'height=0.005', # Make it look like a line. Brilliant!
            'penwidth=0',
            'width=0.1',

        ], ']',
    ] + [
        f'{kids} -> {{{", ".join([escape(p) for p in family.children])}}} [', [
            # TODO: style :child-link color=colora
            f'color="{family.color}"',
            'dir="forward"',
            'arrowhead="tee"',
            'arrowsize=2',
            'weight=2',
        ], ']',
    ]

def renderKidLinks(family, id):
    return [
        '',
        f'{" -> ".join([escape(p) for p in family.children])} [', [
            # style :child-links  before:style:invis ???
            'dir="forward"',
            'arrowhead="tee"',
            'arrowsize=2',
            'weight=2',
            'style="invis"',
        ], ']'
    ]


def renderPerson(data, person, path):
    id = path[-1]
    href = person.get('links',None) and person.links[0]

    unknown = '????-??-??'

    born = person.get('born', None)
    if not born: born = '????'
    else: born = str(born)

    died = person.get('died', None)
    if died is None: died = ''
    elif died is True: died = unknown
    else: died = str(died)

    name = person.get('fullname', None) or person.get('name', None) or id
    surname, firstname = (name.split(',')+[''])[:2]
 
    label = (
      '<<table align="center" border="0" cellpadding="0" cellspacing="2" width="5">\n' +
      '<tr>\n'+
      (
          f'<td rowspan="2" WIDTH="40" HEIGHT="40" FIXEDSIZE="TRUE"><img src="pics/{person.pics[0]}" scale="TRUE"></img></td>'
          if person.get('pics', None) else
          '<td rowspan="2" WIDTH="40" HEIGHT="40" FIXEDSIZE="TRUE" border="1"></td>\n'
      )+
      f'<td align="left" width="100">{firstname}</td>' +
      f'<td align="right" width="100">{surname}</td>' +
      '\n</tr>\n' +
      #'<tr><td align="center">' +
      #'<font point-size="10" color="#aaaaaa">' +
      #`{person.fullname || person.name}</font></td></tr>` +
      '<tr><td colspan="2" align="center">\n' +
      '<font point-size="10" color="#aa7777">' +
      (f'*{born}' if born else '*????-??-??') +
      (f'  +{died}' if died else '') +
      '</font></td></tr>' +
      '</table>>'
      )
    return [
        f'{escape(name)} [', [
        f'label={label}',
        ], ']',
    ]

def renderSubFamilies(data, family, path):
    return sum([
        renderFamily(data, family, f or {}, path+[str(i)])
        for i,f in enumerate(family.get('families',[]))
    ], [])


data = ns.load(sys.argv[1])
p=KinFile(**data)
print(ns(p.dict()).dump())

processFamily(data, data.setdefault('people', ns()))
print(data.dump())
dot = render(data)
print(dot)
Path('output.dot').write_text(dot, encoding='utf8')
graphviz.Source(render(data)).render('output.pdf', format='pdf', view=True)




