import unittest
import b2btest
from .render import indenter, low, render
from .models import Nissaga
from yamlns import namespace as ns

class Indenter_Test(unittest.TestCase):
    def setUp(self):
        self.maxDiff=None

    def test_indenter_emptyList(self):
        result = indenter([])
        self.assertEqual(result, "")

    def test_indenter_string(self):
        result = indenter("hola")
        self.assertEqual(result, "hola")

    def test_indenter_singleItem(self):
        result = indenter(["hola"])
        self.assertEqual(result, "hola")

    def test_indenter_manyItems(self):
        result = indenter(["hola", "bye"])
        self.assertEqual(result,
            "hola\n"
            "bye"
        )

    def test_indenter_innerItem(self):
        result = indenter(["hola", ["hi"], "bye"])
        self.assertEqual(result,
            "hola\n"
            "  hi\n"
            "bye"
        )

    def test_indenter_multilevel(self):
        result = indenter(["hola", ["lev1", ["lev2", ["lev3"], "bye lev2"]], "bye"])
        self.assertEqual(result,
            "hola\n"
            "  lev1\n"
            "    lev2\n"
            "      lev3\n"
            "    bye lev2\n"
            "bye"
        )

    def test_indenter_startOnLevel(self):
        result = indenter([["lev1", ["lev2", ["lev3"], "bye lev2"]], "bye"])
        self.assertEqual(result,
            "  lev1\n"
            "    lev2\n"
            "      lev3\n"
            "    bye lev2\n"
            "bye"
        )

    def test_low(self):
        self.assertEqual(
            low([['a','b'],[],['c','d']]),
            ['a','b','c','d']
        )


class Renderer_Test(unittest.TestCase):
    def setUp(self):
        self.maxDiff=None
        self.b2bdatapath = 'b2bdata'

    def personTemplate(self,
        id="",
        name="",
        surname=" ",
        born="",
        died="",
    ):
        return f"""\
digraph G {{
  edge [
    dir="none"
    color="#cccccc"
  ]
  
  node [
    shape="box"
    style="filled"
    fontname="Helvetica, Arial, sans-serif"
    width=0
    fillcolor="white"
    color="#cccccc"
    margin=0
  ]
  
  rankdir="LR"
  ranksep=0.4
  splines="ortho"
  
  "{id}" [
    label=<<table align="center" border="0" cellpadding="0" cellspacing="1">
<tr>
<td rowspan="3" width="40" height="40" fixedsize="true" bgcolor="#eeeeee"></td>

<td colspan="2">{name}</td>
</tr>
<tr>
<td colspan="2"><font point-size="12" color="#666666">{surname}</font></td>
</tr>
<tr>
<td align="left" width="60"><font point-size="10" color="#aa7777"> {born} </font></td>
<td align="left" width="60"><font point-size="10" color="#aa7777"> {died} </font></td>
</tr>
</table>>
  ]
}}"""

    def test_render_defaultPerson(self):
        tree = Nissaga(**ns.loads("""
            people:
              Alice: {}
        """))
        self.assertEqual(render(tree),
            self.personTemplate(
                id="Alice",
                name="Alice",
        ))

    def test_render_namedPerson(self):
        tree = Nissaga(**ns.loads("""
            people:
              Alice:
                fullname: In Chains, Alice
        """))
        self.assertEqual(render(tree),
            self.personTemplate(
                id="Alice",
                name=" Alice", # TODO: fix strip
                surname="In Chains",
        ))

    def test_render_bornAtDate(self):
        tree = Nissaga(**ns.loads("""
            people:
              Alice:
                born: 2021-01-02
        """))
        self.assertEqual(render(tree),
            self.personTemplate(
                id="Alice",
                name="Alice",
                born="* 2021-01-02",
        ))

    def test_render_born_justDefault(self):
        tree = Nissaga(**ns.loads("""
            people:
              Alice:
                born: true
        """))
        self.assertEqual(render(tree),
            self.personTemplate(
                id="Alice",
                name="Alice",
                born="",
        ))

    def test_render_unborn(self):
        tree = Nissaga(**ns.loads("""
            people:
              Alice:
                born: false
        """))
        self.assertEqual(render(tree),
            self.personTemplate(
                id="Alice",
                name="Alice",
                born="†*",
        ))

    def test_render_bornAnnotation(self):
        tree = Nissaga(**ns.loads("""
            people:
              Alice:
                born: aprox 1987
        """))
        self.assertEqual(render(tree),
            self.personTemplate(
                id="Alice",
                name="Alice",
                born="* aprox 1987",
        ))

    def test_render_died(self):
        tree = Nissaga(**ns.loads("""
            people:
              Alice:
                died: true
        """))
        self.assertEqual(render(tree),
            self.personTemplate(
                id="Alice",
                name="Alice",
                died="†",
        ))

    def test_render_diedFalse_default(self):
        tree = Nissaga(**ns.loads("""
            people:
              Alice:
                died: false
        """))
        self.assertEqual(render(tree),
            self.personTemplate(
                id="Alice",
                name="Alice",
                died="",
        ))

    def test_render_diedAtDate(self):
        tree = Nissaga(**ns.loads("""
            people:
              Alice:
                died: 1888-04-30
        """))
        self.assertEqual(render(tree),
            self.personTemplate(
                id="Alice",
                name="Alice",
                died="† 1888-04-30",
        ))

    def test_render_diedAnnotated(self):
        tree = Nissaga(**ns.loads("""
            people:
              Alice:
                died: aprox 1888
        """))
        self.assertEqual(render(tree),
            self.personTemplate(
                id="Alice",
                name="Alice",
                died="† aprox 1888",
        ))

