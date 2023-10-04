import unittest

import coefficient_calculator
import password


class Tests(unittest.TestCase):

    def test_generator(self):
        self.assertRaises(ValueError, password.generate, '', 1)
        self.assertRaises(ValueError, password.generate, '', -1)

    def test_values(self):
        alphabet='aafsf'
        length=20
        V=100
        T=30
        self.assertEquals(coefficient_calculator.P(alphabet, length, V, T), V * T / (len(alphabet) ** length))
        alphabet = 'aafsasfsaffasfasasfafsf'
        length = 23
        V = 424
        T = 231
        self.assertEquals(coefficient_calculator.P(alphabet, length, V, T), V * T / (len(alphabet) ** length))
