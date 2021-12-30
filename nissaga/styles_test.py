import unittest
from .styles import renderStyle

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
            'attribute="value"'
        ])

    @unittest.skip("Not yet implemented")
    def test_renderStyle_withQuotes(self):
        render = renderStyle(dict(
            attribute = '"value"',
        ))
        self.assertEqual(render, [
            'attribute="\\"value\\""'
        ])

    def test_renderStyle_numeric_quoteless(self):
        render = renderStyle(dict(
            attribute = 32,
        ))
        self.assertEqual(render, [
            'attribute=32'
        ])

    def test_renderStyle_none_ignored(self):
        render = renderStyle(dict(
            attribute = None,
        ))
        self.assertEqual(render, [
        ])




