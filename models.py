import graphviz
from pydantic import BaseModel, Extra, AnyHttpUrl
from yamlns import namespace as ns
from typing import Union, Optional, Dict, List 
import datetime
from consolemsg import warn, step
from pathlib import Path

from render import render

class Person(BaseModel):
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
    people: Dict[str, Person] = ns()

    class Config:
        extra = Extra.forbid

    def normalize(self):
        processFamily(self, self.people)
        #processFamily(data, data.setdefault('people', ns()))



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
    #if 'families' not in family: return
    for family in context.families:
        family.parents = [
            processPerson(parent, people)
            for parent in family.parents
        ]
        print (family.parents)
        family.children = [
            processPerson(child, people)
            for child in family.children or []
        ]
        print (family.children)
        processFamily(family, people)


if __name__ == '__main__':
    import sys

    step("Loading {}...", sys.argv[1])
    data = ns.load(sys.argv[1])

    step("Validating...")
    p=KinFile(**data)

    step("Normalizing...")
    p.normalize()

    #print(data.dump())
    print(ns(p.dict()).dump())

    step("Generating graph...")
    dot = render(p)
    Path('output.dot').write_text(dot, encoding='utf8')

    step("Generating pdf...")
    graphviz.Source(dot).render('output.pdf', format='pdf', view=True)




