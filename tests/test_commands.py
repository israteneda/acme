import unittest
from acme.commands import processing
import contextlib as cl
import io
import re


class TestCommands(unittest.TestCase):

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
            ans = '\nInvalid argument.\nFor more information run: acme --help\n'
            # convert item list to string
            if ''.join(test).startswith('-'):
                self.assertEqual(data, ans)
            else:
                ans = '\nCheck the file is in the same directory\nAlso check the correct file extension (.txt)'  + ans
                self.assertEqual(data, ans)

    def test_acme_file(self):
        test = ['acme/data/employees.txt']
        out = io.StringIO()
        with cl.redirect_stdout(out):
            processing(test)
        data = out.getvalue()
        ans = '\nThe amount to pay RENE is: 215.0 USD\nThe amount to pay ASTRID is: 85.0 USD\nThe amount to pay ERICK is: 395.0 USD\n\n\n'
        self.assertEqual(data, ans)
        pass

    def test_acme_instructions(self):
        test = ['--help']
        out = io.StringIO()
        with cl.redirect_stdout(out):
            processing(test)
        data = re.sub(r'[\n\t\s]', '', out.getvalue())
        with open('tests/data/instructions.txt') as f:
            ans = re.sub(r'[\n\t\s]', '', f.read())
        self.assertEqual(data, ans)
