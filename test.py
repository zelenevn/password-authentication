import re
import unittest
from password import Generator


class TestGUI(unittest.TestCase):
    def setUp(self):
        self.generator = Generator()
        self.numbers = "0123456789"
        self.lower_var = "abcdefghijklmnopqrstuvwxyz"
        self.upper_var = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.symbols_var = "[!#$%&'()*+,-./:;<=>?@[\]^_`{|}~]"

    def test_length_password(self):
        password = self.generator.create_new(5, self.numbers)
        self.assertEquals(len(password), 5)

    def test_button_1(self):
        password = self.generator.create_new(6, self.numbers)
        self.assertTrue(any(x.isdigit() for x in password))

    def test_button_2(self):
        password = self.generator.create_new(4, self.lower_var)
        self.assertTrue(any(x.islower() for x in password))

    def test_button_3(self):
        password = self.generator.create_new(3, self.upper_var)
        self.assertTrue(any(x.isupper() for x in password))

    def test_button_4(self):
        password = self.generator.create_new(2, self.symbols_var)
        self.assertTrue(bool(re.search(self.symbols_var, password)))


if __name__ == "__main__":
    unittest.main()
