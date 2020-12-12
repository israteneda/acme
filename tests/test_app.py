import unittest
from unittest.mock import patch

from acme.app import run, say_hello


class TestScan(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_it_says_hello_to_name(self):
        output: str = say_hello('Monty')

        self.assertEqual('Hello Monty', output)


    @patch('builtins.input', return_value='Monty')
    def test_it_says_hello_to_inputted_name(self, input):
        output: str = run()

        self.assertEqual('Hello Monty', output)


if __name__ == '__main__':
    unittest.main()