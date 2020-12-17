import os
import unittest
from acme.files import get_employees_from_file, get_file_path, read_file_lines


class TestFiles(unittest.TestCase):

    def setUp(self):
        # Check if OS is Windows
        if os.name == 'nt':
            self.employees_get_file_path = 'acme\\data\\employees.txt'
        else:
            self.employees_get_file_path = 'acme/data/employees.txt'

    def test_get_employees_from_file(self):
        employees: str = get_employees_from_file(self.employees_get_file_path)
        employees_names = [employee.name for employee in employees]

        for employee in employees:
            self.assertTrue('RENE' in employees_names)
            self.assertTrue('ASTRID' in employees_names)
            self.assertTrue('WLADYMIR' in employees_names)

    def test_find_file(self):
        current_dir = os.getcwd()
        filepath: str = get_file_path(self.employees_get_file_path)
        expected_file_path: str = os.path.join(
            current_dir, self.employees_get_file_path)

        self.assertEqual(filepath, expected_file_path)

    def test_read_file_lines(self):
        path: str = get_file_path(self.employees_get_file_path)
        file_lines: str = read_file_lines(path)
        with open(path) as file:
            expected_content = file.read()

        self.assertEqual(file_lines, expected_content)
