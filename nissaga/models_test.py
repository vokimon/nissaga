import unittest
from . import models
from yamlns import namespace as ns
from capturer import CaptureOutput

class Nissaga_Test(unittest.TestCase):

    from yamlns.testutils import assertNsEqual

    def setUp(self):
        self.maxDiff = None

    def test_Person_defaults(self):
        p = models.Person()
        self.assertNsEqual(ns(p.model_dump()), self.basePerson())

    def test_Person_overrides(self):
        data = ns.loads("""
            fullname: Perico Palotes
            comment: A comment
        """)
        p = models.Person(**data)
        self.assertNsEqual(ns(p.model_dump()), self.basePerson(
            comment = "A comment",
            fullname = "Perico Palotes",
        ))

    def basePerson(self, **kwds):
        """Single place to change the Person dict default expectation"""
        base = ns.loads("""\
            name: null
            age: null
            alias: null
            born: true
            class_: []
            comment: []
            died: false
            docs: []
            from_: null
            fullname: null
            gender: null
            links: []
            notes: []
            pics: []
            todo: []
        """)
        base.update(**kwds)
        return base

    def baseFamily(self, **kwds):
        """Single place to change the Family dict default expectation"""
        base = ns.loads("""\
            parents: []
            children: []
            divorced: false
            docs: []
            families: []
            house: null
            married: true
            notes: []
        """)
        base.update(**kwds)
        return base

    def baseNissaga(self, **kwds):
        """Single place to change the Nissaga dict default expectation"""
        base = ns.loads("""\
            families: []
            people: {}
            styles: null
        """)
        base.update(**kwds)
        return base

    def assertNormalize(self, input, expected, expected_warnings=[]):
        nissaga = models.Nissaga(**ns.loads(input))

        with CaptureOutput() as errorlog:
            nissaga.normalize()
            warnings =  errorlog.get_lines()
            # KLUDGE: capture library leaves this open
            if errorlog.merged:
                errorlog.output.output_handle.close()
            else:
                errorlog.stdout.output_handle.close()
                errorlog.stderr.output_handle.close()

        data = ns.loads(expected)
        self.assertNsEqual(
            ns(nissaga.model_dump()),
            self.baseNissaga(
                families = [
                    self.baseFamily(**family)
                    for family in data.families
                ],
                people = ns((
                    (id, self.basePerson(**person))
                    for id, person in data.people.items()
                )),
            )
        )
        self.assertEqual(warnings, expected_warnings)

    def test_normalize_parentByName_kept(self):
        self.assertNormalize(
        """
            families:
            - parents:
              - parentid
            people:
              parentid:
                name: Parent Name
        """,
        """\
            families:
            - parents: [parentid]
            people:
              parentid:
                name: Parent Name
        """)

    def test_normalize_childByName_kept(self):
        self.assertNormalize(
        """
            families:
            - children:
              - childid
            people:
              childid:
                name: Child Name
        """,
        """\
            families:
            - children: [childid]
            people:
              childid:
                name: Child Name
        """)

    def test_normalize_inlineParent_moved(self):
        self.assertNormalize(
        """
            families:
            - parents:
              - parentid:
                  name: Parent Name
        """,
        """
            families:
            - parents: [parentid]
            people:
              parentid:
                name: Parent Name
        """)

    def test_normalize_undetailedParent_filledAndWarned(self):
        self.assertNormalize(
        """
            families:
            - parents:
              - parentid
        """,
        """\
            families:
            - parents: [parentid]
            people:
              parentid: {}
        """,
        [
            "\x1b[33mWarning: Person parentid not detailed\x1b[0m"
        ])

    def test_normalize_inlineChild_moved(self):
        self.assertNormalize(
        """
            families:
            - children:
              - childid:
                  name: Child Name
        """,
        """
            families:
            - children: [childid]
            people:
              childid:
                name: Child Name
        """)

    def test_normalize_undetailedChild_filledAndWarned(self):
        self.assertNormalize(
        """
            families:
            - children:
              - childid
        """,
        """
            families:
            - children: [childid]
            people:
              childid: {}
        """,
        [
            "\x1b[33mWarning: Person childid not detailed\x1b[0m"
        ])

    def test_normalize_duppedDetails_warned(self):
        self.assertNormalize(
        """
            families:
            - children:
              - childid:
                  name: Inline Name
            people:
              childid:
                name: Name
        """,
        """\
            families:
            - children: [childid]
            people:
              childid:
                name: Inline Name # TODO: Should it be the not inline one?
        """,
        [
            "\x1b[33mWarning: Person childid specified twice\x1b[0m"
        ])


    def test_normalize_duppedDetailsInline_warned(self):
        self.assertNormalize(
        """
            families:
            - children:
              - personId:
                  name: Inline Children
            - parents:
              - personId:
                  name: Inlined Parent
        """,
        """\
            families:
            - children: [personId]
            - parents: [personId]
            people:
              personId:
                name: Inlined Parent # TODO: Should it be the not inline one?
        """,
        [
            "\x1b[33mWarning: Person personId specified twice\x1b[0m",
        ])

    @unittest.skip("The warning is still not implemented")
    def test_normalize_unrelated_warns(self):
        self.assertNormalize(
        """
            families: []
            people:
              unrelated:
                name: Unrelated Name
        """,
        """\
            families: []
            people:
              unrelated:
                name: Unrelated Name
        """,
        [
            "\x1b[33mWarning: Person personId is unrelated\x1b[0m",
        ])



