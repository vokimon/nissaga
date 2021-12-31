# 0.3.0 2021-12-31

- Better input format documentation
- Person box redesigned:
  - Name on top, below surname, smaller and dimmer
  - remove spurious margins
  - always born and died on the left and right halves
  - Stillborn symbol when `born: false`
- Unions:
  - Bigger family bullet
  - Children node is a small turned triangle
  - Married and divorded dates are not exclusively displayed
  - Less chaotic children links
- Subcommand `scheme` to generate the schema.
- Fix: Person box is a link to person.link[0] if specified
- Fix: Person classes styles are now applied
- Fix: Undetailed persons are warned but properly handled
- Some test coverage added

# 0.2.0 2021-09-23

- Choose the output format at the command line interface
- Accepting gender parameter from some kingraph examples
- Display divorced and married dates at the same time
- Fix: using ids diferent than the fullname, splitted the person
- Fix: Play nice with parentless families

# 0.1.1 2021-09-11

- Packaging and documentation

# 0.1.0 2021-09-11 

- First public release


