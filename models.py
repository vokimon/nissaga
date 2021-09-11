import graphviz
from pydantic import BaseModel, Extra, AnyHttpUrl
from yamlns import namespace as ns
from typing import Union, Optional, Dict, List 
import datetime
from consolemsg import warn
import sys
from pathlib import Path

from render import render

class Person(BaseModel):
    born: Optional[Union[bool, datetime.date, str]] = True
    died: Optional[Union[bool, datetime.date, str]] = False
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
    parents: List[Union[str, Dict[str, Person]]]
    children: Optional[List[Union[str, Dict[str, Person]]]]
    married: Optional[Union[bool, datetime.date, str]] = True
    divorced: Optional[Union[bool, datetime.date, str]] = False
    house: Optional[str]
    notes: Optional[str]
    docs: Optional[List[str]]
    families: Optional[List['Family']] = []

    class Config:
        extra = Extra.forbid

Family.update_forward_refs()
 
class KinFile(BaseModel):
    styles: Dict = None
    families: List[Family] = None
    people: Dict[str, Person] = None

    class Config:
        extra = Extra.forbid


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

def processFamily(data, people):
    if 'families' not in data: return
    for family in data.families:
        family.parents = [
            processPerson(parent, people)
            for parent in family.parents
        ]
        family.children = [
            processPerson(child, people)
            for child in family.get('children', [])
        ]
        processFamily(family, people)



data = ns.load(sys.argv[1])
p=KinFile(**data)
print(ns(p.dict()).dump())

processFamily(data, data.setdefault('people', ns()))
print(data.dump())
dot = render(data)
print(dot)
Path('output.dot').write_text(dot, encoding='utf8')
graphviz.Source(render(data)).render('output.pdf', format='pdf', view=True)




