import unittest

from yamlns.dateutils import Date
from yamlns import namespace as ns
from .models import Person, Nissaga
from .anniversaries import anniversary, personAnniversaries, compileAniversaries


class Anniversary_Test(unittest.TestCase):


    def assertAnniversary(self, today, date, expected, expectedYears):
        result, years = anniversary(date, today)
        self.assertEqual(Date(result), Date(expected))
        self.assertEqual(years, expectedYears)

    def test_anniversary_thisYear(self):
        self.assertAnniversary(
            today = '2010-01-02',
            date = '2001-01-03',
            expected = '2010-01-03',
            expectedYears = 9,
        )

    def test_anniversary_nextYear(self):
        self.assertAnniversary(
            today = '2010-05-02',
            date = '2001-05-01',
            expected = '2011-05-01',
            expectedYears = 10,
        )

    def test_anniversary_sameDay(self):
        self.assertAnniversary(
            today = '2021-09-01',
            date = '2010-09-01',
            expected = '2021-09-01',
            expectedYears = 11,
        )

    def test_personAnniversaries_birthDate(self):
        person = Person(
            name = 'Alice',
            born = Date('2010-01-02'),
        )
        self.assertEqual(
            personAnniversaries('alice', person, Date('2021-09-01')),
            [
                (Date('2022-01-02'), "Alice will turn 12."),
            ]
        )

    def test_personAnniversaries_died(self):
        person = Person(
            name = 'Alice',
            born = Date('2010-02-01'),
            died = True,
        )
        self.assertEqual(
            personAnniversaries('alice', person, '2021-09-01'),
            [
                (Date('2022-02-01'), "Alice would have turned 12."),
            ]
        )

    def test_personAnniversaries_diedAtDate(self):
        person = Person(
            name = 'Alice',
            born = Date('2010-02-01'),
            died = Date('2021-01-04'),
        )
        self.assertEqual(
            personAnniversaries('alice', person, '2021-09-01'),
            [
                (Date('2022-02-01'), "Alice would have turned 12."),
                (Date('2022-01-04'), "It will be 1 years since Alice passed away."),
            ]
        )

    def test_compileAnniversaries(self):
        nissaga = Nissaga(**ns.loads("""
        people:
          alice:
            born: 2001-03-01
          barbara:
            died: 2017-07-30
        """))
        self.assertEqual(
            compileAniversaries(nissaga, Date('2021-03-31')),
            [
                (Date('2022-03-01'), "alice will turn 21."),
                (Date('2021-07-30'), "It will be 4 years since barbara passed away."),
            ]
        )



