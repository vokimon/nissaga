from unittest import TestCase
from . import models
from yamlns import namespace as ns
from capturer import CaptureOutput

class Nissaga_Test(TestCase):

    from yamlns.testutils import assertNsEqual

    def setUp(self):
        self.maxDiff = None

    def test_Person_defaults(self):
        p = models.Person()
        self.assertNsEqual(ns(p.dict()), """
            age: null
            alias: null
            class_: []
            comment: []
            died: false
            born: true
            docs: []
            from_: null
            fullname: null
            gender: null
            links: []
            name: null
            notes: []
            pics: []
            todo: []
        """)

    def test_Person_overrides(self):
        data = ns.loads("""
            fullname: Perico Palotes
            comment: A comment
        """)
        p = models.Person(**data)
        self.assertNsEqual(ns(p.dict()), """
            age: null
            alias: null
            class_: []
            comment: A comment
            died: false
            born: true
            docs: []
            from_: null
            fullname: Perico Palotes
            gender: null
            links: []
            name: null
            notes: []
            pics: []
            todo: []
        """)

    def basePerson(self, **kwds):
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
        base = ns.loads("""\
            families: []
            people: {}
            styles: null
        """)
        base.update(**kwds)
        return base

    def assertNormalizedNissaga(self, nissaga, expected):
        data = ns.loads(expected)
        self.assertNsEqual(
            ns(nissaga.dict()),
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

    def test_normalize_parentByName_kept(self):
        data = ns.loads("""
            families:
            - parents:
              - parentid
            people:
              parentid:
                name: Parent Name
        """)
        n = models.Nissaga(**data)
        n.normalize()

        self.assertNormalizedNissaga(n, """\
            families:
            - parents: [parentid]
            people:
              parentid:
                name: Parent Name
        """)

    def test_normalize_childByName_kept(self):
        data = ns.loads("""
            families:
            - children:
              - childid
            people:
              childid:
                name: Child Name
        """)
        n = models.Nissaga(**data)
        n.normalize()

        self.assertNormalizedNissaga(n, """\
            families:
            - children: [childid]
            people:
              childid:
                name: Child Name
        """)

    def test_normalize_inlineParent_moved(self):
        data = ns.loads("""
            families:
            - parents:
              - parentid:
                  name: Parent Name
        """)
        n = models.Nissaga(**data)
        n.normalize()

        self.assertNormalizedNissaga(n, """\
            families:
            - parents: [parentid]
            people:
              parentid:
                name: Parent Name
        """)

    def test_normalize_undetailedParent_filledAndWarned(self):
        data = ns.loads("""
            families:
            - parents:
              - parentid
        """)
        n = models.Nissaga(**data)

        with CaptureOutput() as errorlog:
            n.normalize()
            self.assertEqual(errorlog.get_lines(), [
                "\x1b[33mWarning: Person parentid not detailed\x1b[0m"
            ])

        self.assertNormalizedNissaga(n, """\
            families:
            - parents: [parentid]
            people:
              parentid: {}
        """)
    def test_normalize_inlineChild_moved(self):
        data = ns.loads("""
            families:
            - children:
              - childid:
                  name: Child Name
        """)
        n = models.Nissaga(**data)
        n.normalize()

        self.assertNormalizedNissaga(n, """\
            families:
            - children: [childid]
            people:
              childid:
                name: Child Name
        """)

    def test_normalize_undetailedChild_filledAndWarned(self):
        data = ns.loads("""
            families:
            - children:
              - childid
        """)
        n = models.Nissaga(**data)

        with CaptureOutput() as errorlog:
            n.normalize()
            self.assertEqual(errorlog.get_lines(), [
                "\x1b[33mWarning: Person childid not detailed\x1b[0m"
            ])

        self.assertNormalizedNissaga(n, """\
            families:
            - children: [childid]
            people:
              childid: {}
        """)

    def test_normalize_duppedDetails_warned(self):
        data = ns.loads("""
            families:
            - children:
              - childid:
                  name: Inline Name
            people:
              childid:
                name: Name
        """)
        n = models.Nissaga(**data)

        with CaptureOutput() as errorlog:
            n.normalize()
            self.assertEqual(errorlog.get_lines(), [
                "\x1b[33mWarning: Person childid specified twice\x1b[0m"
            ])

        self.assertNormalizedNissaga(n, """\
            families:
            - children: [childid]
            people:
              childid:
                name: Inline Name # TODO: Should it be the not inline one?
        """)



