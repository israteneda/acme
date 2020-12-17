import unittest
from acme.domain.shift import Shift
from acme.domain.working_hours import WorkingHours


class TestWorkingHours(unittest.TestCase):

    def setUp(self):
        self.working_hours = WorkingHours('01:00-03:00')
        self.shift = Shift(name='first_shift', hours='00:01-09:00')

    def test_start_time_is_between(self):
        is_between = self.working_hours.start_time_is_between(self.shift)

        self.assertTrue(is_between)

    def test_check_hours_exception(self):
        with self.assertRaises(SystemExit) as cm:
            wrong_working_hours = WorkingHours('00:00-03:00')

        self.assertEqual(cm.exception.code, 1)

        with self.assertRaises(SystemExit) as cm:
            wrong_working_hours = WorkingHours('25:00-40:00')

        self.assertEqual(cm.exception.code, 1)

        with self.assertRaises(SystemExit) as cm:
            wrong_working_hours = WorkingHours('04:00-03:00')

        self.assertEqual(cm.exception.code, 1)
