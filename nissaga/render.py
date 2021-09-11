from yamlns import namespace as ns
from .styles import applyStyles

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
        state = (
            '⚮' if family.divorced is True else (
            f'⚮ {family.divorced}' if family.divorced is not False else (
            '⚯' if family.married is False else (
            '' if family.married is True else (
            f'⚭ {family.married}'
        )))))

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
                ':parent-link',
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

    born = person.born
    if born is None: born = '????'
    elif born is True: born = '????'
    else: born = str(born)

    died = person.died
    if died is None: died = ''
    elif died is False: died = ''
    elif died is True: died = unknown
    else: died = str(died)

    name = person and person.fullname or person.name or id
    surname, firstname = (name.split(',')+[''])[:2]
 
    label = (
      '<<table align="center" border="0" cellpadding="0" cellspacing="2" width="5">\n' +
      '<tr>\n'+
      (
          f'<td rowspan="2" WIDTH="40" HEIGHT="40" FIXEDSIZE="TRUE"><img src="pics/{pic}" scale="TRUE"></img></td>'
          if pic else
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

def renderSubFamilies(root, family, path):
    return low(
        renderFamily(root, family, f or {}, path+[str(i)])
        for i,f in enumerate(family.families or [])
    )


