from yamlns import namespace as ns
from .styles import applyStyles
import datetime

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

def escape(s):
    # TODO: review this
    if type(s)==str:
        return '"'+s+'"'
    return s

def formatdate(date):
    if not isinstance(date, datetime.date):
        return date
    return f"{date:%Y-%m-%d}"

def low(lines):
    "Reduces a level of sublisting"
    return sum((l for l in lines), [])

def indenter(lines, spacer='  '):
    "Considers each level of sublisting an indented block"

    def subindenter(lines, level=-1):
        if type(lines) == str:
            return [level*spacer + lines]
        return low(
            subindenter(element, level+1)
            for element in lines
        )

    return '\n'.join(subindenter(lines))

def render(root):
    return indenter([
        'digraph G {', [
            'edge [',
                applyStyles(root, ':edge'),
            ']',
            '',
            'node [',
                applyStyles(root, ':node'),
            ']',
            '',
            ] + applyStyles(root, ':digraph') + [
            '',
        ]+
        low(
            renderFamily(root, root, f, [str(i)])
            for i,f in enumerate(root.families or [])
        )+
        low(
            renderPerson(root, p, [str(n)])
            for i,(n,p) in enumerate((root.people or ns()).items())
        ),
        '}'
    ])


def renderFamily(root, house, family, path):

    def renderHousePrelude(family, path):
        if not family.house:
            return []
        return [
            '#'*76,
            f'# House {".".join(path)} - {family.house}',
            '#'*76,
            '',
            f'label=<<b>{family.house}</b>>',
            #f'labelhref="{family.links and family.links[0]}"',
            ] + applyStyles(root, ':house',
                post=dict(
                    color="#fafafa" if not len(path)&1 else "#f4f4f4"
                )
            ) + [
            '',
        ]

    def renderParents(family, id):
        if not family.parents:
            return ['# No parents']

        union = f'union_{id}'
        state = []
        married = formatdate(family.married)
        if married is False:
            state.append('⚯')
        elif married is not True:
            state.append(f'⚭ {married}')

        divorced = formatdate(family.divorced)
        if divorced is True:
            state.append('⚮')
        elif divorced is not False:
            state.append(f'⚮ {divorced}')

        state = '\n'.join(state)

        return [
            f'{union} [',
            f'xlabel="{state}"' if state else [],
            applyStyles(root, ':union', pre=dict(
                fillcolor=familyColor,
            )),
            ']',
            '',
        ] + ([
            f'{{{", ".join([escape(p) for p in family.parents])}}} -> {union} [',
            applyStyles(root, ':parent-link', pre=dict(
                color=familyColor,
            )),
            ']',
        ] if family.parents else [])

    def renderLink(family, id):
        if not family.parents: return []
        if not family.children: return []

        return [
          f'union_{id} -> siblings_{id} [',
            applyStyles(root,
                ':parent-child-link', 
                pre=dict(
                    color=familyColor
                ),
            ),
          ']',
        ]

    def renderKids(family, id):
        if not family.children:
            return ['# No children']

        kids = f'siblings_{id}'
        union = f'union_{id}'
        return [
            f'{kids} [',
            applyStyles(root, ':children', pre=dict(fillcolor=familyColor),
            ),
            ']',
        ] + [
            f'{kids} -> {{{", ".join([escape(p) for p in family.children])}}} [',
            applyStyles(root, ':child-link', pre=dict(color=familyColor)),
            ']',
        ]

    # TODO: Unused
    def renderKidLinks(family, id):
        return [
            '',
            f'{" -> ".join([escape(p) for p in family.children])} [',
            applyStyles(root, ':child-link', pre=dict(style='invis')),
            ']'
        ]

    familyColor = familyColors[ int(path[-1]) % len(familyColors) ]
    slug='_'.join(str(p) for p in path)
    jointparents = ', '.join([p for p in family.parents or [] if p]) or "none"
    jointchildren = ', '.join([p for p in family.children or [] if p]) or "none"
    return [
        f'subgraph cluster_family_{slug} {{', [
            ] + applyStyles(root, ':family') + [
            '',
            ] +
            renderHousePrelude(family, path) +
            renderSubFamilies(root, family, path) +
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


def renderPerson(root, person, path):
    id = path[-1]
    unknown = '????-??-??'

    if not person:
        person=ns(
            born=None,
            died=None,
            fullname=id,
            links=[],
            pics=[],
        )

    href = person.links and person.links[0]
    pic = person.pics and person.pics[0]

    born = formatdate(person.born)
    if born is False or born == 0: born = '†*' # stillborn
    elif born is None: born = '' # just as True, the default
    elif born is True or born == 1: born = '' # born
    else: born = f"* {born}"

    died = formatdate(person.died)
    if died is None: died = '' # Not specified
    elif died is False or died == 0: died = '' # Explicit alive
    elif died is True or died == 1: died = "†" # Dead but no date
    else: died = f"† {died}"

    name = person and person.fullname or person.name or id
    surname, firstname = ([' ']+name.split(','))[-2:]
    picsize = 40, 40 # TODO: configurable
    label = "\n".join([
      '<table align="center" border="0" cellpadding="0" cellspacing="1">',
      '<tr>',
      (
          f'<td rowspan="3" width="{picsize[0]}" height="{picsize[1]}" fixedsize="true"><img src="pics/{pic}" scale="TRUE"></img></td>'
          if pic else
          f'<td rowspan="3" width="{picsize[0]}" height="{picsize[1]}" fixedsize="true" bgcolor="#eeeeee"></td>'
      ),
      f'<td colspan="2">{firstname}</td>',
      "</tr>",
      "<tr>",
      f'<td colspan="2"><font point-size="12" color="#666666">{surname}</font></td>',
      '</tr>',
      '<tr>',
      f'<td align="left" width="60"><font point-size="10" color="#aa7777"> {born} </font></td>',
      f'<td align="left" width="60"><font point-size="10" color="#aa7777"> {died} </font></td>',
      '</tr>',
      '</table>',
    ])
    link = f'URL="{person.links[0]}"' if person.links else []
    return [
        f'{escape(id)} [', [
            link,
            low([
                applyStyles(root, cls)
                for cls in person.class_
            ]),
            f'label=<{label}>',
        ],']',
    ]

def renderSubFamilies(root, family, path):
    return low(
        renderFamily(root, family, f or {}, path+[str(i)])
        for i,f in enumerate(family.families or [])
    )


