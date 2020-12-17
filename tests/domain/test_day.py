import unittest
from acme.domain.day import Day


class TestDay(unittest.TestCase):

    def setUp(self):
        self.day = Day('MO')

    def test_calculate_day_cost(self):
        day_cost: float = self.day.calculate_day_cost('10:00-12:00')
        self.assertEqual(day_cost, 30.0)
        day_cost: float = self.day.calculate_day_cost('8:00-17:00')
        self.assertEqual(day_cost, 145.0)
