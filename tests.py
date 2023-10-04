import unittest

import errors
from generator import Generator


class Tests(unittest.TestCase):

    def test_password_generator(self):

        self.assertEquals(Generator('', 10).get_password(), errors.ALPHABET_LENGTH_ERROR)
        self.assertEquals(Generator('ss', -10).get_password(), errors.PASSWORD_LENGTH_ERROR)
        self.assertEquals(Generator('ss', 0).get_password(), errors.PASSWORD_LENGTH_ERROR)
        self.assertEquals(Generator('', 0).get_password(), errors.ALPHABET_AND_PASWORD_LENGTH_ERROR)


