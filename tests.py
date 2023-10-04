import string
import unittest
from password_generator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):

    def test_password_length(self):
        # Проверяем разные длины пароля от 6 до 15 символов
        for length in range(6, 15):
            generator = PasswordGenerator(length)
            # Проверим, что длина сгенерированного пароля соответствует ожидаемой
            self.assertEqual(generator.length, length)

    def test_generate_password(self):
        # Проверяем разные комбинации трёх алфавитов
        generator = PasswordGenerator(12)

        # Проверка, что есть хотя бы одна из каждой выбранной группы
        password = generator.generate_password("1234")
        self.assertEqual(len(password), 12)
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_alphabet_size(self):
        # Проверяем, что общее количество символов в алфавите больше 30
        generator = PasswordGenerator(10)
        total_alphabet_size = sum(len(generator.groups[group]) for group in "1234")
        self.assertGreater(total_alphabet_size, 30)


if __name__ == '__main__':
    unittest.main()
