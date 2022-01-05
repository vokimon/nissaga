from yamlns.dateutils import Date

def anniversary(date, today=None):
    """Given the date of an event, returns a tuple of the next
    anniversary of the event and how many years it will turn.
    """
    today = Date(today) if today else Date.today()
    date = Date(date)
    result = Date(today.year, date.month, date.day)
    if result < today:
        result = Date(result.year+1, date.month, date.day)
    return result, result.year - date.year

def personAnniversaries(id, person, today):
    result = []
    name = person.fullname or person.name or id
    if isinstance(person.born, Date):
        date, years = anniversary(person.born, today)
        if person.died:
            result.append((date, f"{name} would have turned {years}."))
        else:
            result.append((date, f"{name} will turn {years}."))
    if isinstance(person.died, Date):
        date, years = anniversary(person.died, today)
        result.append((date, f"It will be {years} years since {name} passed away."))
    return result

def compileAniversaries(nissaga, today=None):
    return sum([
        personAnniversaries(id, person, today)
        for id, person in nissaga.people.items()
    ],[])


