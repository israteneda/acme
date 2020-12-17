import unittest
from acme import utils


class TestUtils(unittest.TestCase):

    def test_get_times(self):
        start_time, end_time = utils.get_times('10:00-12:00')

    def test_get_hours(self):

        expected_hours = '05:00-07:00'
        hours = utils.get_hours('MO05:00-07:00')

        self.assertEqual(hours, expected_hours)

    def test_get_day_abbrev(self):

        expected_day_abbrev = 'MO'
        day = utils.get_day_abbrev('MO05:00-07:00')

        self.assertEqual(day, expected_day_abbrev)

    def test_get_datatimes(self):

        expected_days = ['MO05:00-07:00', 'TU10:00-12:00']
        datatimes = utils.get_datatimes('MO05:00-07:00,TU10:00-12:00')

        self.assertEqual(datatimes, expected_days)

    def test_get_lines(self):

        expected_lines = ['RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',
                          'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']
        lines = utils.get_lines(
            'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\nASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00')

        self.assertEqual(lines, expected_lines)

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

    def test_wrong_time_range(self):
        pass

        with self.assertRaises(SystemExit) as cm:
            utils.wrong_time_range(4, 3)

        self.assertEqual(cm.exception.code, 1)

    def test_hours_to_string(self):

        expected_hours = '20:00'
        hours = utils.hours_to_string(20.0)

        self.assertEqual(hours, expected_hours)
        
        expected_hours = '00:00'
        hours = utils.hours_to_string(0)

        self.assertEqual(hours, expected_hours)
