import unittest
from .styles import renderStyle, combineStyles
from .models import Nissaga
from yamlns import namespace as ns

class Styles_Test(unittest.TestCase):

    def test_renderStyle_empty(self):
        render = renderStyle(dict())
        self.assertEqual(render, [
        ])

    def test_renderStyle_oneValue(self):
        render = renderStyle(dict(
            attribute = 'value',
        ))
        self.assertEqual(render, [
            'attribute="value"',
        ])

    def test_renderStyle_manyValues(self):
        render = renderStyle(dict(
            attribute = 'value',
            attribute2 = 'value2',
        ))
        self.assertEqual(render, [
            'attribute="value"',
            'attribute2="value2"',
        ])

    @unittest.skip("Not yet implemented")
    def test_renderStyle_withQuotes(self):
        render = renderStyle(dict(
            attribute = '"value"',
        ))
        self.assertEqual(render, [
            'attribute="\\"value\\""',
        ])

    def test_renderStyle_numeric_quoteless(self):
        render = renderStyle(dict(
            attribute = 32,
        ))
        self.assertEqual(render, [
            'attribute=32',
        ])

    def test_renderStyle_none_ignored(self):
        render = renderStyle(dict(
            attribute = None,
        ))
        self.assertEqual(render, [
        ])

    def setupClasses(self, content="{}"):
        return Nissaga(styles=ns.loads(content))

    from yamlns.testutils import assertNsEqual

    def test_combineStyles_empty(self):
        tree = self.setupClasses()
        result = combineStyles(
            tree,
        )
        self.assertNsEqual(result, ns())

    def test_combineStyles_pre(self):
        tree = self.setupClasses()
        result = combineStyles(tree,
            pre=ns(
                preattribute='value',
            ),
        )
        self.assertNsEqual(result, """\
            preattribute: value
        """)

    def test_combineStyles_post(self):
        tree = self.setupClasses()
        result = combineStyles(tree,
            post=ns(
                postattribute='value',
            ),
        )
        self.assertNsEqual(result, """\
            postattribute: value
        """)

    def test_combineStyles_post_overwritesPre(self):
        tree = self.setupClasses()
        result = combineStyles(tree,
            pre=ns(
                overwritten='ignored',
            ),
            post=ns(
                overwritten='final',
            ),
        )
        self.assertNsEqual(result, """\
            overwritten: final
        """)

    def test_combineStyles_classStyles_taken(self):
        tree = self.setupClasses("""
            class1:
              preattribute1: class1value
              postattribute1: class1value
            class2:
              preattribute2: class2value
              postattribute2: class2value
            
        """)
        result = combineStyles(tree,
            'class1',
            pre=ns(
                preattribute1='prevalue',
                preattribute2='prevalue',
            ),
            post=ns(
                postattribute1='postvalue',
                postattribute2='postvalue',
            ),
        )
        self.assertNsEqual(result, """\
          preattribute1: class1value # set by class
          postattribute1: postvalue # set by class but overwritten
          preattribute2: prevalue # not set by class, pre kept
          postattribute2: postvalue # not set by class, pre kept
        """)

    def test_combineStyles_defaults(self):
        tree = self.setupClasses()
        result = combineStyles(tree,
            ':digraph',
            pre=ns(
                rankdir="caca", # ignored
            ),
            post=ns(
            ),
        )
        self.assertNsEqual(result, """\
            rankdir: LR
            ranksep: 0.4
            splines: ortho
        """)

    def test_combineStyles_defaults_modified(self):
        tree = self.setupClasses("""
            :digraph:
              rankdir: TL # overwrites
              styleattribute: value
        """)
        result = combineStyles(tree,
            ':digraph',
            pre=ns(
                preattribute='prevalue', # merged
                rankdir='caca', # ignored
            ),
            post=ns(
                splines='polylines',
            ),
        )
        self.assertNsEqual(result, """\
            preattribute: prevalue # from pre
            rankdir: TL            # from style, overwrite
            styleattribute: value  # from style
            ranksep: 0.4           # from default
            splines: polylines     # from post, overwrite
        """)






