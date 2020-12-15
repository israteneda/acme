import io
import os
import re
import unittest
from acme.commands import processing
import contextlib as cl


class TestCommands(unittest.TestCase):

    def setUp(self):
        # Check if SO is Windows
        if os.name == 'nt':
            self.salary_file_path = 'data\\salaries.txt'
            self.employees_file_path = 'acme\\data\\employees.txt'
        else:
            self.salary_file_path = 'data/salaries.txt'
            self.employees_file_path = 'acme/data/employees.txt'

    def test_processing_wrong_arguments(self):
        tests = [
            ['-casdfdsa'],
            ['data.bin'],
            ['-helpasd'],
        ]
        for test in tests:
            out = io.StringIO()
            with cl.redirect_stdout(out):
                processing(test)
            data = out.getvalue()
            err = 'Invalid argument.\nFor more information run: acme --help\n'
            self.assertEqual(data, err)

    def test_acme_command(self):
        test = [self.employees_file_path]
        out = io.StringIO()
        with cl.redirect_stdout(out):
            processing(test)
        data = out.getvalue()
        # Read sample salaries
        file_path = os.path.dirname(os.path.realpath(__file__))
        path: str = os.path.join(file_path, self.salary_file_path)
        with open(path) as file:
            content = file.read()

        self.assertEqual(data, content)

    def test_acme_instructions(self):
        test = ['--help']
        out = io.StringIO()
        with cl.redirect_stdout(out):
            processing(test)
        data = re.sub(r'[\n\t\s]', '', out.getvalue())
        with open('tests/data/instructions.txt') as f:
            ans = re.sub(r'[\n\t\s]', '', f.read())
        self.assertEqual(data, ans)
