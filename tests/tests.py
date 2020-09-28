import unittest

from app.api import countries, country, totals, us_states


class ApplicationTests(unittest.TestCase):

    def test_countries(self):
        json = countries(sort_by="Cases")
        self.assertIsNotNone(json)

    def test_country(self):
        json = country("Ireland")
        self.assertIsNotNone(json)

    def test_totals(self):
        json = totals()
        self.assertIsNotNone(json)

    def test_us_states(self):
        json = us_states(sort_by="Cases")
        self.assertIsNotNone(json)
