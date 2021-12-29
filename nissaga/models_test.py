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


