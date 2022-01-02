import unittest
from .cli import app
from typer.testing import CliRunner
from pathlib import Path
import consolemsg

yaml="""\
families:
- parents:
  - alice
- children:
  - barbara
people:
  alice: {}
  barbara: {}
"""

import sys

class Cli_Test(unittest.TestCase):

    def assertFiles(self, expected):
        self.assertEqual(
            list(sorted(str(x) for x in Path().glob('*'))),
            expected,
        )
    def clearConsolemsg(self):
        # KLUDGE: consolemsg caches wrapped stdin and stdout
        # and makes click invoke not to work.
        if hasattr(consolemsg.stderr, 'cached'):
            delattr(consolemsg.stderr, 'cached')
        if hasattr(consolemsg.stdout, 'cached'):
            delattr(consolemsg.stdout, 'cached')

    def setUp(self):
        self.clearConsolemsg()
        self.runner = CliRunner()

    def tearDown(self):
        self.clearConsolemsg()

    def chtempdir(self):
        return self.runner.isolated_filesystem()

    def test_schema_defaultYaml(self):
        with self.chtempdir() as path:
            result = self.runner.invoke(app, [
                'schema',
                'yaml',
            ])
            self.assertEqual(result.output, (
                "\x1b[34;1m:: Generating 'nissaga-schema.yaml'\x1b[0m\n"
            ))
            self.assertFiles([
                'nissaga-schema.yaml',
            ])
            self.assertEqual(result.exit_code, 0)

    def test_schema_json(self):
        with self.chtempdir() as path:
            result = self.runner.invoke(app, [
                'schema',
                'json',
            ])
            self.assertFiles([
                'nissaga-schema.json',
            ])
            self.assertEqual(result.exit_code, 0)
            self.assertEqual(result.output, (
                "\x1b[34;1m:: Generating 'nissaga-schema.json'\x1b[0m\n"
            ))

    def test_draw_pdf(self):
        with self.chtempdir() as path:
            Path('alice.yaml').write_text("""
            families:
            - children: [alice]
            people:
                alice: {}
            """, encoding='utf8')
            result = self.runner.invoke(app, [
                'draw',
                'alice.yaml',
            ])
            self.assertEqual(result.output, (
                "\x1b[34;1m:: Validating...\x1b[0m\n"
                "\x1b[34;1m:: Normalizing...\x1b[0m\n"
                "\x1b[34;1m:: Generating graph...\x1b[0m\n"
                "\x1b[34;1m:: Generating alice.pdf...\x1b[0m\n"
                ))
            self.assertFiles([
                'alice.pdf',
                'alice.yaml',
            ])
            self.assertEqual(result.exit_code, 0)

    def test_draw_svg(self):
        with self.chtempdir() as path:
            Path('alice.yaml').write_text("""
            families:
            - children: [alice]
            people:
                alice: {}
            """, encoding='utf8')
            result = self.runner.invoke(app, [
                'draw',
                'alice.yaml',
                'svg',
            ])
            self.assertEqual(result.output, (
                "\x1b[34;1m:: Validating...\x1b[0m\n"
                "\x1b[34;1m:: Normalizing...\x1b[0m\n"
                "\x1b[34;1m:: Generating graph...\x1b[0m\n"
                "\x1b[34;1m:: Generating alice.svg...\x1b[0m\n"
                ))
            self.assertFiles([
                'alice.svg',
                'alice.yaml',
            ])
            self.assertEqual(result.exit_code, 0)

    def test_draw_dot(self):
        with self.chtempdir() as path:
            Path('alice.yaml').write_text("""
            families:
            - children: [alice]
            people:
                alice: {}
            """, encoding='utf8')
            result = self.runner.invoke(app, [
                'draw',
                'alice.yaml',
                'svg',
            ])
            self.assertEqual(result.output, (
                "\x1b[34;1m:: Validating...\x1b[0m\n"
                "\x1b[34;1m:: Normalizing...\x1b[0m\n"
                "\x1b[34;1m:: Generating graph...\x1b[0m\n"
                "\x1b[34;1m:: Generating alice.svg...\x1b[0m\n"
                ))
            self.assertFiles([
                'alice.svg',
                'alice.yaml',
            ])
            self.assertEqual(result.exit_code, 0)



