# Pending tasks

- [ ] Make the schema documentation to work on github
- [ ] Implement parents2 and children2 used in kingraph
- [ ] Make pets part of the family
- [ ] CLI: Controlling the output filename
- [ ] CLI: Enable or disabling autoview
- [ ] When Python<=3.7, use `from __future__ import annotations` to define Family inline https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
- [ ] Scaping quotes and other characters
- [ ] class attribute keept on dot, so that svg has it
- [ ] Coverage: born: None
- [ ] Coverage: died: None
- [ ] Coverage: escape without quotes
- [ ] Normalize: Warn unrelated persons
- [ ] Review: on dupped person details, which version should prevail?
- [ ] Configuration framework
- [ ] Config: formats: output formats to use when no format specified by cli (default: pdf)
- [ ] Config: dateformat: date format to display, defaut ISO-8601 ("%Y-%m-%d", resulting in YYYY-MM-DD)
- [ ] Config: avatarsize: tuple (width, height) in pixels in which to embed the avatar picture
- [ ] Config: persontemplate: being able to personalize
- [ ] Config: picdir: prefix to the pics
- [ ] Config: docdir: prefix to the docs
- [ ] CLI documentation: typer nissaga.cli utils docs --output cli.md

# Done

- [x] Coverage: parents and children
- [x] Coverage: unmarried
- [x] Coverage: married at date
- [x] Coverage: divorced
- [x] Coverage: divorced at date
- [x] Coverage: combine divorced and married
- [x] Remove unused renderKidsLinks
- [x] Coverage: house
- [x] Coverage: subfamily
- [x] Coverage: subhouse
- [x] Coverage: normalize inlined parent
- [x] Coverage: normalize unspecified parent
- [x] Coverage: normalize inlined child
- [x] Coverage: normalize unspecified child
- [x] Coverage: normalize dupped details
- [x] Coverage: dupped two inline
- [x] Redundant: RenderKids when no kids
