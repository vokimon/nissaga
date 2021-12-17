# Nissaga, genealogy tree generator

## About

Nissaga can be used to generate Genealogy trees
from a simple data description in yaml, following a format
which extends the one used by [kingraph].

## Installation

```bash
pip install nissaga
```

You need to install [graphviz]. Not the python wrapper library, but the program itself.

[kingraph]: https://github.com/rstacruz/kingraph
[graphviz]: https://graphviz.org

## Usage

The command line interface is still quite simple and
future versions will evolve it to a more powerful one.
Right now it works like this:

```bash
nissaga myfamily.yaml
```

This generates a file `myfamily.pdf`

You can specify a second parameter to choose the output format: png, svg or any supported by graphviz.

```bash
nissaga myfamily.yaml svg
```

## Input file

The input file follows this [Schema](docs/schema_doc.html)

In order to regenerate this documentation

```bash
pip install json-schema-for-humans
cd docs
generate-schema-doc ../nissaga-schema.json
```


## Differences with kingraph

This application was started as a clone of the functionality of kingraph
to overcome the performance and scalability problems with big trees,
but also extending the functionality.

The following kingraph features are not supported:

- `family.children2` and `family.parents2` relations are not yet supported

The following features have been introduced by nissaga, and are not available in kingraph (but the yaml would be still compatible).

- Rich **person boxes** with dates, photos and separated first name and surname.
	- `person.born` maybe set to a date, and will appear as `*YYYY-MM-DD` bellow the person's name.
	- `person.died` maybe set to a date or true and will appear as `+YYYY-MM-DD` bellow the person's name.
	- `person.age` age of dead, not used, just to keep track of it when that's the only data we have.
	- `person.pics` is a list of pictures files relative to the yaml file. The first one will be added as person's face. The other pics are not used yet.
- Rich **unions** with marriage and divorce annotations
	- `family.married`: defaults to true. Set it to false to indicate unmarried patnership (`⚯`). Set it to a date to see `⚭YYYY-MM-DD` in the union node.
	- `family.divorced`: defaults to false. Set it to true to indicate a divorce (`⚮`). Set it to a date to see `⚮YYYY-MM-DD` in the union node.
- Attributes for **internal documentation**:
	- `person.todo` a string or list of strings of pending tasks for the person
	- `person.from` origin of the person (country, city...)
	- `person.comments` a string or list of strings of comments
	- `family.notes` a string or list of strings of notes
	- `family.docs` documentation about the family. A list of document paths relative to the yaml file. Not used yet but it is suposed to provide links to the research sources.





