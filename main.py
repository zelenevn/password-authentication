from generate_password import *


def interface():
    while True:
        len_pass_str = input("Введите желаемую длину пароля: ")
        len_pass = int(len_pass_str)

        num_selected_groups = []
        for element in input(
                """Введите через пробел желаемые алфавиты для пароля:\n0: a-z,\n1: A-Z,\n2: 0-9\n3: спец. смволы\n"""
        ).split():
            num_selected_groups.append(int(element))
        try:
            print("Пароль: " + generate_password(len_pass, num_selected_groups))
            break
        except ValueError:
            print('Пароль должен содержать не менее трех групп символов и быть длиннее 6 символов')

    print("Сложность пароля:" + password_complexity(len_pass, num_selected_groups))

    return len_pass, num_selected_groups


if __name__ == '__main__':
    interface()
