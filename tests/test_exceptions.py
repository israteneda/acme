import unittest
from acme.expections import MalformedFileError, WrongTimeRangeError


class TestExceptions(unittest.TestCase):

    def test_malformed_file_error(self):
        with self.assertRaises(SystemExit) as cm:
            raise MalformedFileError('Error obtaining name')

        self.assertEqual(cm.exception.code, 1)

    def test_wrong_time_range_error(self):
        with self.assertRaises(SystemExit) as cm:
            raise WrongTimeRangeError(4.0, 0.3)

        self.assertEqual(cm.exception.code, 1)
