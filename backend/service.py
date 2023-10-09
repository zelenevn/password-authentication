import random
import string


def generate_password(min_: int = 15, max_: int = 24):
    letters = string.ascii_letters + string.digits + "_-."
    random_password = ''.join(random.choice(letters) for i in range(random.randint(min_, max_)))
    return random_password


# # Пробный вариант основанный на генерации uuid
# def generate_password_uuid(num=None, letters=None):
#     """
#     - Длина пароля не менее 6 символов;
#     - Алфавит пароля не менее 30 символов;
#     - Пароль не должен содержать личных данных пользователя;
#     - Пароль не должен быть словом из какого-либо словаря;
#     - Пароль не должен состоять из повторяющихся букв;
#     - Пароль не должен состоять из символов, соответствующих подряд идущим клавишам на клавиатуре (QWERTY);
#     - Желательно включать в пароль символы в разных регистрах;
#
#     - Максимальное количество неуспешных попыток аутентификации до блокировки от 3 до 10 попыток;
#     - Блокировка программно-технического средства или учетной записи пользователя в случае достижения
#     установленного максимального количества неуспешных попыток аутентификации от 3 до 15 минут;
#     - Смена паролей не более чем через 180 дней.
#     :return:
#     """
#     import uuid
#
#     if num is not None and num < 6:
#         return "Password must be more than 6 characters"
#
#     # Генерация пароля
#     password = str(uuid.uuid4())
#     # Кол-во букв в строке
#     letters_index = [i for i, c in enumerate(password) if c.isalpha()]
#     # Кол-во символов, которые превратятся в верхний регистр
#     count_rand_index = random.randint(len(letters_index) // 4, len(letters_index) // 2)
#     for i in range(count_rand_index):
#         index = random.choice(letters_index)
#         letters_index.remove(index)
#         password = password[:index] + password[index].upper() + password[index + 1:]
#
#     return password
