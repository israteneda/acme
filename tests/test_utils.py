import unittest
from acme import utils


class TestUtils(unittest.TestCase):

    def test_get_times(self):
        start_time, end_time = utils.get_times('10:00-12:00')

    def test_get_datetimes(self):

        expected_hours = '05:00-07:00'
        hours = utils.get_datetimes('MO05:00-07:00')

        self.assertEqual(hours, expected_hours)

    def test_get_day_abbrev(self):

        expected_day_abbrev = 'MO'
        day = utils.get_day_abbrev('MO05:00-07:00')

        self.assertEqual(day, expected_day_abbrev)

    def test_get_employee_name(self):

        expected_name = 'ASTRID'
        name = utils.get_employee_name(
            'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00')

        self.assertEqual(name, expected_name)

    def test_get_week_worked(self):

        expected_week = 'MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'
        week_worked = utils.get_week_worked(
            'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00')

        self.assertEqual(week_worked, expected_week)

    def test_to_decimal_hours(self):

        expected_decimal = 10.0
        decimal_hours = utils.to_decimal_hours('10:00')

        self.assertEqual(decimal_hours, expected_decimal)

    def test_hours_to_string(self):

        expected_hours = '20:00'
        hours = utils.hours_to_string(20.0)

        self.assertEqual(hours, expected_hours)
        
        expected_hours = '00:00'
        hours = utils.hours_to_string(0)

        self.assertEqual(hours, expected_hours)
