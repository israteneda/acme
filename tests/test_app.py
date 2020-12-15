import unittest
import os
from unittest.mock import patch

from acme.app import file_path, read_file_lines, calculate_salary, show_salary, calculate_day_cost

# TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'testdata.html')


class TestApp(unittest.TestCase):

    # def setUp(self):
    #    self.testdata = open(TESTDATA_FILENAME).read()

    # def test_find_file(self):
    #     output: str = file_path('data.txt')

    #     self.assertEqual('I:\\Code\\acme\\data.txt', output)

    def test_read_file_lines(self):
        path: str = file_path('acme/data/employees.txt')
        output: str = read_file_lines(path)

        self.assertEqual(
            'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n'
            'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00\n'
            'ERICK=MO5:00-11:00,TH8:00-17:00,SU01:00-05:00', output)

    def test_name_in_the_output(self):
        path: str = file_path('acme/data/employees.txt')
        output: str = show_salary('acme/data/employees.txt')

        self.assertRegex(output, 'RENE')
        self.assertRegex(output, 'ASTRID')
        self.assertRegex(output, 'ERICK')

    def test_calculate_salary_amount(self):
        output: float = calculate_salary(
            'MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00')
        self.assertEqual(215.0, output)
        output: float = calculate_salary(
            'MO10:00-12:00,TH12:00-14:00,SU20:00-21:00')
        self.assertEqual(85.0, output)
        output: float = calculate_salary(
            'MO5:00-11:00,TH8:00-17:00,SU01:00-05:00')
        self.assertEqual(395.0, output)

    def test_calculate_day_cost(self):
        output: float = calculate_day_cost('MO', '10:00-12:00')
        self.assertEqual(30.0, output)
        output: float = calculate_day_cost('SU', '20:00-21:00')
        self.assertEqual(25.0, output)


if __name__ == '__main__':
    unittest.main()
