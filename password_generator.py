import math
import random
import string


def password_entropy(password, total_alphabet_length):
    # Расчет информационной энтропии
    entropy = len(password) * math.log2(total_alphabet_length)
    # Определение уровня сложности пароля на основе информационной энтропии
    if entropy < 35:
        return "Слабая"
    elif 35 <= entropy < 60:
        return "Средняя"
    elif 60 <= entropy < 128:
        return "Высокая"
    else:
        return "Очень высокая"


class PasswordGenerator:
    alphabets = {
        1: string.ascii_lowercase,
        2: string.ascii_uppercase,
        3: string.digits,
        4: string.punctuation
    }

    def __init__(self, length=0, selected_alphabets=None):
        self._length = length
        self._selected_alphabets = selected_alphabets if selected_alphabets else []

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value < 6:
            raise ValueError('Пароль должен быть не менее 6 символов')
        self._length = value

    @property
    def selected_alphabets(self):
        return self._selected_alphabets

    @selected_alphabets.setter
    def selected_alphabets(self, value):
        if len(value) < 2:
            raise ValueError('Алфавит пароля должен содержать не менее двух групп символов')
        self._selected_alphabets = value

    def generate_password(self):
        # Подготовка всех символов и общей длины алфавита
        while True:
            all_chars = ''
            total_alphabet_length = 0
            for alphabet_id in self.selected_alphabets:
                if alphabet_id in self.alphabets:
                    alphabet = self.alphabets[alphabet_id]
                    all_chars += alphabet
                    total_alphabet_length += len(alphabet)

            # Генерация пароля
            password = ''.join(random.choice(all_chars) for _ in range(self.length))

            has_all_alphabets = all(
                any(char in self.alphabets[alphabet_id] for char in password) for alphabet_id in
                self.selected_alphabets)

            if has_all_alphabets:
                break

        # Оценка сложности пароля на основе информационной энтропии
        complexity = password_entropy(password, total_alphabet_length)

        return password, complexity
