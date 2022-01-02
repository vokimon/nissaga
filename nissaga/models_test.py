from unittest import TestCase
from . import models
from yamlns import namespace as ns

class KinFile_Test(TestCase):

    from yamlns.testutils import assertNsEqual

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

    def test_Nissaga_normalize_moveInlinePersonDefinitions(self):
        self.maxDiff = None
        data = ns.loads("""
            families:
            - parents:
              - parent
              - inlineParent:
                  name: Inline Parent
              - unspecifiedParent
              children:
              - child
              - inlineChild:
                  name: Inline Child
              - unspecifiedChild
            people:
              parent:
                name: Specified Parent
              child:
                name: Specified Child
        """)
        n = models.Nissaga(**data)
        n.normalize()
        self.assertNsEqual(ns(n.dict()),"""\
            styles: null # autofilled
            families:
            - parents:
              - parent
              - inlineParent
              - unspecifiedParent
              children:
              - child
              - inlineChild
              - unspecifiedChild

              # Autofilled
              divorced: false
              docs: []
              families: []
              house: null
              married: true
              notes: []

            people:
              parent:
                name: Specified Parent
                # Autofilled
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
              child:
                name: Specified Child
                # Autofilled
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
              unspecifiedParent:
                # Autofilled
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
              unspecifiedChild:
                # Autofilled
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
              inlineParent:
                name: Inline Parent
                # Autofilled
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
              inlineChild:
                name: Inline Child
                # Autofilled
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


