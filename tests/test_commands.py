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

        # Get the console output
        out = io.StringIO()
        with cl.redirect_stdout(out):
            processing(test)
        content = out.getvalue()

        # Read sample salaries
        file_path = os.path.dirname(os.path.realpath(__file__))
        path: str = os.path.join(file_path, self.salary_file_path)
        with open(path) as file:
            expected_content = file.read()

        self.assertEqual(content, expected_content)

    def test_acme_instructions(self):
        test = ['--help']

        # Get the console output
        out = io.StringIO()
        with cl.redirect_stdout(out):
            processing(test)
        instructions = re.sub(r'[\n\t\s]', '', out.getvalue())

        # Read instructions
        with open('tests/data/instructions.txt') as f:
            expected_instructions = re.sub(r'[\n\t\s]', '', f.read())

        # Allow long text
        self.maxDiff = None

        self.assertEqual(instructions, expected_instructions)

    def test_acme_demo_command(self):
        test = ['--demo']

        # Get the console output
        out = io.StringIO()
        with cl.redirect_stdout(out):
            processing(test)
        demo_content = out.getvalue()

        # Read sample employees data
        file_path = os.path.dirname(os.path.realpath(__file__))
        path: str = os.path.join(file_path, self.salary_file_path)
        with open(path) as file:
            expected_content = file.read()

        self.assertEqual(demo_content, expected_content)
