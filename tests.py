import unittest
from password_generator import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password_valid_length(self):
        password_generator = PasswordGenerator()

        # Попробуем разные длины пароля от 6 до 20 символов
        for length in range(6, 21):
            password_generator.length = length
            password_generator.selected_alphabets = [1, 2, 3]  # Выбираем группы символов
            password, _ = password_generator.generate_password()

            # Проверим, что длина сгенерированного пароля соответствует ожидаемой
            self.assertEqual(len(password), length)

    def test_generate_password_invalid_length(self):
        password_generator = PasswordGenerator()

        # Попробуем длины пароля менее 6 символов
        invalid_lengths = [0, 1, 2, 3, 4, 5]

        for length in invalid_lengths:
            with self.assertRaises(ValueError):
                password_generator.length = length
                password_generator.selected_alphabets = [1, 2, 3]  # Выбираем группы символов
                password_generator.generate_password()

    def test_alphabet_count(self):
        password_generator = PasswordGenerator()

        # Попробуем разные комбинации трех алфавитов
        alphabet_combinations = [
            [1, 2], [1, 3], [1, 4],
            [2, 3], [2, 4],
            [3, 4]
        ]

        for alphabets in alphabet_combinations:
            password_generator.selected_alphabets = alphabets

            # Проверим, что общее количество символов в алфавите больше 30
            total_chars = sum(len(password_generator.alphabets[alphabet_id]) for alphabet_id in alphabets)
            self.assertGreater(total_chars, 30)


if __name__ == '__main__':
    unittest.main()
