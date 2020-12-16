import os
import sys
import unittest
from acme.app import get_file_path, read_file_lines, calculate_salary, get_employees, calculate_day_cost


class TestApp(unittest.TestCase):

    def setUp(self):
        # Check if OS is Windows
        if os.name == 'nt':
            self.employees_get_file_path = 'acme\\data\\employees.txt'
        else:
            self.employees_get_file_path = 'acme/data/employees.txt'

    def test_find_file(self):
        current_dir = os.getcwd()
        filepath: str = get_file_path(self.employees_get_file_path)
        expected_file_path: str = os.path.join(current_dir, self.employees_get_file_path)

        self.assertEqual(filepath, expected_file_path)

    def test_read_file_lines(self):
        path: str = get_file_path(self.employees_get_file_path)
        file_lines: str = read_file_lines(path)
        with open(path) as file:
            expected_content = file.read()

        self.assertEqual(file_lines, expected_content)

    def test_names_in_the_output(self):
        path: str = get_file_path(self.employees_get_file_path)
        employees: str = get_employees(self.employees_get_file_path)
        employees_names = [employee.name for employee in employees]

        self.assertTrue('RENE' in employees_names)
        self.assertTrue('ASTRID' in employees_names)
        self.assertTrue('WLADYMIR' in employees_names)

    def test_calculate_salary_amount(self):
        salary: float = calculate_salary(
            'MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00')
        self.assertEqual(salary, 215.0)
        salary: float = calculate_salary(
            'MO10:00-12:00,TH12:00-14:00,SU20:00-21:00')
        self.assertEqual(salary, 85.0)
        salary: float = calculate_salary(
            'MO5:00-11:00,TH8:00-17:00,SU01:00-05:00')
        self.assertEqual(salary, 395.0)

    def test_calculate_day_cost(self):
        day_cost: float = calculate_day_cost('MO', '10:00-12:00')
        self.assertEqual(day_cost, 30.0)
        day_cost: float = calculate_day_cost('SU', '20:00-21:00')
        self.assertEqual(day_cost, 25.0)
        day_cost: float = calculate_day_cost('TU', '8:00-17:00')
        self.assertEqual(day_cost, 145.0)


if __name__ == '__main__':
    unittest.main()
