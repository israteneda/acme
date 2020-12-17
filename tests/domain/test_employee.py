import unittest
from acme.domain.employee import Employee


class TestEmploye(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('ASTRID')

    def test_calculate_salary_amount(self):
        salary: float = self.employee.calculate_salary(
            'MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00')
        self.assertEqual(salary, 215.0)
        salary: float = self.employee.calculate_salary(
            'MO10:00-12:00,TH12:00-14:00,SU20:00-21:00')
        self.assertEqual(salary, 85.0)
        salary: float = self.employee.calculate_salary(
            'MO5:00-11:00,TH8:00-17:00,SU01:00-05:00')
        self.assertEqual(salary, 395.0)

    def test_calculate_salary_amount_exception(self):
        with self.assertRaises(SystemExit) as cm:
            self.employee.calculate_salary('MO10:00-12:00,,')

        self.assertEqual(cm.exception.code, 1)
