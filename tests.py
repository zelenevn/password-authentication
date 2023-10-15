import re
import unittest

import alphabet_gen
import password_gen


class Test(unittest.TestCase):

    def test_password_length(self):
        password = password_gen.generate(33, password_gen.Alphabet.value)
        self.assertEquals(len(password), 33)

    def test_alphabet_length(self):
        alphabet = alphabet_gen.generate(22)
        self.assertEquals(len(alphabet), 22)

    def test_all_symbols_available(self):
        password = password_gen.generate(22, password_gen.Alphabet.value)
        self.assertTrue(password.isupper() and password.islower() and password.isdigit() and password.isalnum())
