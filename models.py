from pydantic import BaseModel, Extra, AnyHttpUrl
from yamlns import namespace as ns
from typing import Union, Optional, Dict, List 
import datetime
from consolemsg import warn
import sys


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

    class Config:
        extra = Extra.forbid
        fields = dict(
            from_ = 'from',
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

    class Config:
        extra = Extra.forbid



def addPerson(person, persons):
    if type(person) is str:
        if person not in persons:
            persons[person] = None
        return person

    for name, p in person.items():
        if persons.get(name, None) is not None:
            warn(f"Person {name} specified twice")
        persons[name] = p
        return name


def processPerson(person, persons):
    return addPerson(person, persons)

def processFamily(data, persons):
    if 'families' not in data: return
    for family in data.families:
        family.parents = [
            processPerson(parent, persons)
            for parent in family.parents
        ]
        family.children = [
            processPerson(child, persons)
            for child in family.get('children', [])
        ]
        processFamily(family, persons)




data = ns.load(sys.argv[1])
p=KinFile(**data)
print(ns(p.dict()).dump())

persons = ns()
processFamily(data, persons)
print(persons.dump())
print(data.dump())



