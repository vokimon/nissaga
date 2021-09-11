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
    notes: Optional[str]
    alias: Optional[str]
    from_: Optional[str]
    todo: Optional[Union[str,List[str]]]
    pics: Optional[List[str]]
    docs: Optional[List[str]]
    links: Optional[List[str]] #Optional[List[AnyHttpUrl]]
    class_: Optional[List[str]]

    class Config:
        extra = Extra.forbid
        fields = dict(
            from_ = 'from',
            class_ = 'class',
        )

class Family(BaseModel):
    """Represents a family kernel with parents and children and any descendant family"""
    parents: List[Union[str, Dict[str, Person]]]
    children: Optional[List[Union[str, Dict[str, Person]]]]
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
    """Represents the data required to build a family tree"""
    styles: Dict = None
    families: List[Family] = None
    people: Dict[str, Person] = ns()

    class Config:
        extra = Extra.forbid

    def normalize(self):
        processFamily(self, self.people)


def processPerson(person, people):
    if type(person) is str:
        if person not in people:
            people[person] = None
        return person

    for name, p in person.items():
        if people.get(name, None) is not None:
            warn(f"Person {name} specified twice")
        people[name] = p
        return name

def processFamily(context, people):
    for family in context.families:
        family.parents = [
            processPerson(parent, people)
            for parent in family.parents
        ]
        family.children = [
            processPerson(child, people)
            for child in family.children or []
        ]
        processFamily(family, people)

def schema():
    return KinFile.schema_json(indent=2)



