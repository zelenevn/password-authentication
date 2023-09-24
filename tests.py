import unittest

import errors
from application import App
from password_generator import Password_generator


class Tests(unittest.TestCase):

    def test_password_generator(self):
        self.assertEquals(Password_generator('', 10).generate(), errors.ALPHABET_LENGTH_ERROR)
        self.assertEquals(Password_generator('ss', -10).generate(), errors.PASSWORD_LENGTH_ERROR)
        self.assertEquals(Password_generator('ss', 0).generate(), errors.PASSWORD_LENGTH_ERROR)
        self.assertEquals(Password_generator('', 0).generate(), errors.ALPHABET_AND_PASWORD_LENGTH_ERROR)


