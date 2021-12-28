import graphviz
from pydantic import BaseModel, Extra, AnyHttpUrl
from yamlns import namespace as ns
from typing import Union, Optional, Dict, List 
import datetime
from consolemsg import warn, step
from pathlib import Path

from .render import render

class Person(BaseModel):
    """Represents the data of a person"""
    fullname: Optional[str]
    name: Optional[str]
    born: Optional[Union[bool, int, datetime.date, str]] = True
    died: Optional[Union[bool, int, datetime.date, str]] = False
    age: Optional[int]
    comment: Optional[Union[str,List[str]]]
    notes: Optional[Union[str,List[str]]]
    alias: Optional[str]
    from_: Optional[str]
    todo: Optional[Union[str,List[str]]]
    pics: Optional[List[str]]
    docs: Optional[List[str]]
    links: Optional[List[str]] #Optional[List[AnyHttpUrl]]
    gender: Optional[str]
    class_: Optional[List[str]] = []

    class Config:
        extra = Extra.forbid
        fields = dict(
            from_ = 'from',
            class_ = 'class',
        )

# You can reference persons by its id but you an also define them inline 
PersonRef = Union[str, Dict[str, Person]]

class Family(BaseModel):
    """Represents a family kernel with parents and children and any descendant family"""
    parents: Optional[List[PersonRef]]
    children: Optional[List[PersonRef]]
    married: Optional[Union[bool, int, datetime.date, str]] = True
    divorced: Optional[Union[bool, int, datetime.date, str]] = False
    house: Optional[str]
    notes: Optional[str]
    docs: Optional[List[str]]
    families: Optional[List['Family']] = []

    class Config:
        extra = Extra.forbid

Family.update_forward_refs()
 
class KinFile(BaseModel):
    """Top level element containing the data required to build a family tree"""
    styles: Dict = None
    families: List[Family] = None
    people: Dict[str, Person] = ns()

    class Config:
        extra = Extra.forbid

    def normalize(self):
        processFamily(self, self.people)
        instantianteUndetailedPersons(self.people)

def instantianteUndetailedPersons(persons):
    for id, person in persons.items():
        if person is not None: continue
        warn(f"Person {id} not detailed")
        persons[id] = Person()


def processPerson(person, people):
    if type(person) is str:
        if person not in people:
            people[person] = None
        return person

    for id, p in person.items():
        if people.get(id, None) is not None:
            warn(f"Person {id} specified twice")
        people[id] = p
        return id

def processFamily(context, people):
    for family in context.families:
        family.parents = [
            processPerson(parent, people)
            for parent in family.parents or []
        ]
        family.children = [
            processPerson(child, people)
            for child in family.children or []
        ]
        processFamily(family, people)

def schema_json():
    return KinFile.schema_json(indent=2)

def schema_yaml():
    return ns(KinFile.schema()).dump()



