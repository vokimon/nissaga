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

    def test_render_defaultPerson(self):
        tree = Nissaga(**ns.loads("""
            people:
              Alice: {}
        """))
        self.assertB2BEqual(render(tree))

    def test_render_namedPerson(self):
        tree = Nissaga(**ns.loads("""
            people:
              Alice:
                fullname: In Chains, Alice
        """))
        # "In Chains" should be added in the second row
        self.assertB2BEqual(render(tree))

    def test_render_bornAtDate(self):
        tree = Nissaga(**ns.loads("""
            people:
              Alice:
                born: 2021-01-01
        """))
        # "In Chains" should be added in the second row
        self.assertB2BEqual(render(tree))



