import string
import unittest

import errors
from generator import Generator


class Tests(unittest.TestCase):

    def test_alphabet1(self):
        self.assertEquals(Generator('', 20).get_password(), errors.ALPHABET_LENGTH_ERROR)

    def test_length1(self):
        self.assertEquals(Generator(string.ascii_lowercase, -1).get_password(), errors.PASSWORD_LENGTH_ERROR)

    def test_length2(self):
        self.assertEquals(Generator(string.ascii_lowercase, 0).get_password(), errors.PASSWORD_LENGTH_ERROR)

    def test_complex(self):
        self.assertEquals(Generator('', -2).get_password(), errors.ALPHABET_AND_PASWORD_LENGTH_ERROR)



