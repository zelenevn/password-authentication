import random
import string

class PasswordGenerator:
    def durability(self, time, speed):  # Количественная оценка стойкости парольной защиты
        alpha_size = sum(len(self.groups[group]) for group in self.groups)
        password_space = alpha_size ** self.length
        t_in_day = 24 * 60  # Количество минут в дне
        probability = (speed * time * t_in_day) / password_space
        return probability

    # Задание групп символов, которые могут использоваться при генерации пароля
    def __init__(self, length=12):
        self.length = length
        self.groups = {
            '1': string.ascii_lowercase,  # Группа 1: строчные буквы (a-z)
            '2': string.ascii_uppercase,  # Группа 2: заглавные буквы (A-Z)
            '3': string.digits,           # Группа 3: цифры (0-9)
            '4': string.punctuation       # Группа 4: специальные символы (например, !@#$%^&*)
        }

    def generate_password(self, selected_groups="1234"):
        selected_groups = set(selected_groups)

        if not selected_groups:
            raise ValueError("Ошибка: Выберите хотя бы одну группу символов")

        password = []

        # Гарантия хотя бы одного символа из каждой выбранной группы
        for group in selected_groups:
            if group in self.groups:
                password.append(random.choice(self.groups[group]))

        # Заполняем остаток пароля случайными символами
        remaining_length = self.length - len(password)  # оставшаяся длина
        if remaining_length > 0:
            # Создаём алфавит, объединяя символы из выбранных групп
            alphabet = "".join(self.groups[group] for group in selected_groups if group in self.groups)
            # Добавляем случайные символы к паролю, чтобы достичь требуемой длины
            password.extend(random.choice(alphabet) for _ in range(remaining_length))
        random.shuffle(password)  # смиволы в случайном порядке
        return ''.join(password)
