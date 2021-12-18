# Nissaga input format

Nissaga input format is a YAML with the following content:

## Kinfile

Root node containing the information required to generate the family tree.

- **people:** `map(id -> Person)` Persons details. Details can be also inlined in the family specification.
- **families:** `list(Family)` Relatives information.
- **styles:** `map(selector -> Style)` Graphviz attributes to apply to each selector.

## Family

Relatives information. A family is a set of (maybe unkwown) parents and children.
Subfamilies can be defined when children become parents in their own families.
Subfamilies enables write the yaml using a tree like the resulting one
but using them is not required.

- **parents:** `list[id|map(id -> Person)` The parents of the family (you can use the id or detail the person inline)
- **children:** `list[id|map(id -> Person)` The children of the family (you can use the id or detail the person inline)
- **married:** `bool|int|Date|str` (Default: true) Date of marriage
	- If False, is an unmarried couple
	- If True, the default, just married unknown date
	- If a Date, the date is shown on the family node with the married simbol
	- Any other text just shows it besides the marriage symbol
- **divorced:** `bool|int|Date|str` (Default: false) Date of divorce
	- If False, the default, nothing is shown
	- If True, a divorce symbol is shown on the family dot
	- If a date or a text, it is shown besides the divorce symbol
- **house:** `str` House the family belongs to. It is represented by a labeled box containing the persons.
- **notes:** `str` Any note regarding the marriage
- **docs:** `list[files]` A list of files serving as documentation for the information
- **families:** `list[Family]` Sub families

## Person

Person details. They can be specified both in `people` or inline in `parents`, `children` instead of using just the id.

- **name:** `str` TODO: Explain difference between id, name, fullname and alias.
- **fullname:** `str` Surnames are placed first, followed by a comma and then the first name.
- **alias:** `str`
- **from:** `str` Place of origin. Just for the record, not shown.
- **gender:** `str` male|female|neutral. Not used yet
- **born:** `bool|int|Date|str` (Default: true) Date of birth
	- If False, is an stillborn
	- If True, the default, the date is unkwown, nothin is shown
	- If a Date, the date is shown preceded of the `*`
	- Any other text just shows it besides the `*`
- **died:** `bool|int|Date|str` (Default: false) Date of death
	- If False, the default, nothing is shown
	- If True, a divorce symbol is shown on the family dot
	- If a date or a text, it is shown besides the divorce symbol
- **age:** `int` Age at death. Sometimes is the only data available. For the record, not shown.
- **links:** `List[URL]` Links related to the person. By clicking on the person, the first one will be followed.
- **notes:** `str|List[str]` Any notes regarding the person
- **comment:** `str|List[str]` Any comments regarding the person information gathering
- **todo:** `str|List[str]` A list of pending tasks about the person information gathering
- **docs:** `list[files]` A list of files serving as documentation for the information
- **pics:** `list[files]` A list of image files containing pictures of the person.
  The first one will be used as avatar.





