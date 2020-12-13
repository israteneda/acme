import unittest
import os
from unittest.mock import patch

from acme.app import file_path, read_file_lines, calculate_salary, show_salary, calculate_day_cost


class TestApp(unittest.TestCase):

    # def test_find_file(self):
    #     output: str = file_path('data.txt')

    #     self.assertEqual('I:\\Code\\acme\\data.txt', output)

    def test_read_file_lines(self):
        path: str = file_path('data.txt')
        output: str = read_file_lines(path)

        self.assertEqual(
            'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n'
            'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00', output)

    def test_show_name_in_the_output(self):
        path: str = file_path('data.txt')
        output: str = show_salary()

        self.assertRegex(output, 'RENE')
        self.assertRegex(output, 'ASTRID')
    
    def test_calculate_salary_amount(self):
        output: float = calculate_salary('MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00')
        self.assertEqual(215, output)
        output: float = calculate_salary('MO10:00-12:00,TH12:00-14:00,SU20:00-21:00')
        self.assertEqual(85, output)

    def test_calculate_day_cost(self):
        output: float = calculate_day_cost('MO', '10:00-12:00')

        self.assertEqual(30, output)


if __name__ == '__main__':
    unittest.main()
