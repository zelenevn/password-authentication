import unittest

from backend.service import generate_password


class TestPassword(unittest.TestCase):

    def test_length(self):
        # Проверка, что длина пароля соответствует заданным параметрам
        self.assertEqual(13, len(generate_password(13, 13)))
        self.assertEqual(21, len(generate_password(21, 21)))

    def test_available_characters(self):
        # Проверка, что символы пароля входят в доступный набор
        ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-.'
        password = generate_password()

        for char in password:
            self.assertIn(char, ascii_letters)


if __name__ == '__main__':
    unittest.main()
