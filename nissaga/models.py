import graphviz
from pydantic import BaseModel, Extra, AnyHttpUrl, Field
from yamlns import namespace as ns
from typing import Union, Optional, Dict, List 
import datetime
from consolemsg import warn, step
from pathlib import Path

from .render import render

Event = Union[
    bool, # Has happened or not
    int, # Year it happenned
    datetime.date, # Full date it happened
    str, # Any other annotation
]

class Person(BaseModel):
    """Represents the data of a person"""
    fullname: Optional[str] = Field(None, description=(
        "Surnames are placed first, followed by a comma and then the first name. "
        "If no comma, it is just considered the first name"
    ))
    name: Optional[str] = Field(None, description=(
        "TODO: Explain difference between id, name, fullname and alias. "
    ))
    alias: Optional[str] = Field(None, description=(
        "TODO: Explain difference between id, name, fullname and alias. "
    ))
    born: Optional[Event] = Field(True, description=(
        "Date of birth or false to indicate stillborn, or true to indicate unknown date "
        "or a year or a string annotation."
    ))
    died: Optional[Event] = Field(False, description=(
        "Date of death of true to indicate dead but unknown date "
        "or a year or a string annotation."
    ))
    age: Optional[int] = Field(None, description=(
        "Age at death, instead of `died`. "
        "Just for the record, not shown. "
        "Sometimes is the only information available in gravestones."
    ))
    from_: Optional[str] = Field(None, description=(
        "Place of origin. "
        "Just for the record, not shown."
    ))
    comment: Optional[Union[str,List[str]]] = Field([], description=(
        "Any comments regarding the person information gathering. "
        "Just for the record, not shown."
    ))
    notes: Optional[Union[str,List[str]]] = Field([], description=(
        "Any comments regardin the person."
        "Just for the record, not shown."
    ))
    todo: Optional[Union[str,List[str]]] = Field([], description=(
        "A list of pending tasks about the person information gathering. "
        "Just for the record, not shown."
    ))
    pics: Optional[List[str]] = Field([], description=(
        "A list of image files containing pictures of the person. "
        "The first one is used as avatar and it should have an almost squared aspect ratio."
    ))
    docs: Optional[List[str]] = Field([], description=(
        "A list of files serving as documentation of the gathered information."
    ))
    links: Optional[List[AnyHttpUrl]] = Field([], description=(
        "A list of links related to the person. "
        "Clicking on the person box will go to the first one."
    ))
    gender: Optional[str] = Field(None, description=(
        "Not used yet."
    ))
    class_: Optional[List[str]] = Field([], description=(
        "Space separated style classes for the person. "
        "Specific attributes can be specified for the persons having a given class."
    ))

    class Config:
        extra = Extra.forbid
        fields = dict(
            from_ = 'from',
            class_ = 'class',
        )

# You can reference persons by its id but you can also
# define them inline with a single item dict.
PersonRef = Union[str, Dict[str, Person]]


class Family(BaseModel):
    """Represents a family kernel with parents and children and any descendant family"""
    parents: Optional[List[PersonRef]] = Field([], description=(
        "Parents of the family. "
        "You can use the person's id, or detail the person inline."
    ))
    children: Optional[List[PersonRef]] = Field([], description=(
        "Children of the family. "
        "You can use the person's id, or detail the person inline."
    ))
    married: Optional[Event] = Field(True, description=(
        "Date of marriage. "
        "False to indicate unmarried couple, or true to indicate unknown date "
        "or a year or a string annotation after the marriage symbol."
    ))
    divorced: Optional[Event] = Field(False, description=(
        "Date of divorce. "
        "If false, the default, nothing is shown. "
        "Set to true to show a divorce symbol. "
        "If it is a date, an integer (year) or any other string, "
        "will be displayeed after the divorce symbol."
    ))
    house: Optional[str] = Field(None, description=(
        "House the family belongs to. "
        "It is represented by a labeled gray box grouping the persons"
    ))
    notes: Optional[Union[str,List[str]]] = Field([], description=(
        "Any comments regardin the family."
        "Just for the record, not shown."
    ))
    docs: Optional[List[str]] = Field([], description=(
        "A list of files serving as documentation of the gathered information."
    ))
    families: Optional[List['Family']] = Field([], description=(
        "Subfamilies. "
        "They can be defined when children become parents in their own families. "
        "Nesting is not mandatory, just to keep data in a tree like structure if you prefer that. "
        "You could alternatively define children's families at the same level."
    ))

    class Config:
        extra = Extra.forbid

Family.update_forward_refs()
 
class Nissaga(BaseModel):
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
    return Nissaga.schema_json(indent=2)

def schema_yaml():
    return ns(Nissaga.schema()).dump()



