import secrets as s
import string

LOWERCASE = string.ascii_lowercase  # алфавит маленьких букв
UPPERCASE = string.ascii_uppercase  # алфавит больших букв
DIGITS = string.digits  # алфавит цифр
PUNCTUATION = string.punctuation  # алфавит спецсимволов

ALL_SYMBOLS = [LOWERCASE, UPPERCASE, DIGITS, PUNCTUATION]  # список всех алфавитов


def make_groups_distribution(count_groups: int, len_pass: int) -> list:
    """Функция, генерирующая количество символов в пароле каждого вида, принимает номера алфавитов и длину пароля"""
    groups_distribution = list()

    for i in range(count_groups, 1, -1):
        num_symbol = s.SystemRandom().randint(
            1,
            len_pass - i + 1 - sum(groups_distribution)
        )
        groups_distribution.append(num_symbol)
    groups_distribution.append(len_pass - sum(groups_distribution))
    return groups_distribution


def generate_password(len_pass: int, num_selected_groups: list):
    """функция, принимающая необходимую длину пароля и требуемые символы"""
    groups_distribution = make_groups_distribution(  # словарь вида номер группы: количество символов в пароле
        count_groups=len(num_selected_groups),
        len_pass=len_pass)

    parts_password = list()

    for i, num in enumerate(
            num_selected_groups):  # i - индекс алфавита в groups_distribution, num - индекс алфавита в ALL_SYMBOLS
        count = groups_distribution[i]  # получаем количество символов данной группы для пароля
        parts_password.append(
            ''.join([s.choice(ALL_SYMBOLS[num]) for _ in range(count)])  # генерируем пароль
        )

    pre_ready_password = ''.join(parts_password)  # создаем парольную строку

    return ''.join(
        s.SystemRandom().sample(
            pre_ready_password, k=len(pre_ready_password)  # перемешиваем строку
        )
    )


def interface():
    len_pass_str = input("Введите желаему длину пароля: ")
    len_pass = int(len_pass_str)

    num_selected_groups = []
    for element in input("""Введите через пробел желаемые алфавиты для пароля:
                        0: a-z,
                        1: A-Z,
                        2: 0-9
                        3: спец. смволы
                        """).split():
        num_selected_groups.append(int(element))

    return len_pass, num_selected_groups


if __name__ == '__main__':
    len_pass, num_selected_groups = interface()
    print("Пароль: " + generate_password(len_pass, num_selected_groups))
