# `nissaga`

Nissaga is a genealogy tree generator

**Usage**:

```console
$ nissaga [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `draw`: Draws the tree for the input file
* `schema`: Dumps the schema for the input files

## `nissaga draw`

Draws the tree for the input file

**Usage**:

```console
$ nissaga draw [OPTIONS] YAMLFILE [FORMAT]:[pdf|svg|png|dot|jpg]...
```

**Arguments**:

* `YAMLFILE`: Input yaml file to process  [required]
* `[FORMAT]:[pdf|svg|png|dot|jpg]...`: Output formats, pdf if not specified

**Options**:

* `--help`: Show this message and exit.

## `nissaga schema`

Dumps the schema for the input files

**Usage**:

```console
$ nissaga schema [OPTIONS] [FORMAT]:[json|yaml]
```

**Arguments**:

* `[FORMAT]:[json|yaml]`: Format  [default: yaml]

**Options**:

* `--help`: Show this message and exit.

