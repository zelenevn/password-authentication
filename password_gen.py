import enum
import random
import string


class Alphabet(enum.Enum):

    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    punctuation = string.punctuation
    digits = string.digits


def error_processing(length):
    if not length.isdigit():
        return "Ошибка ввода длины пароля. Длина пароля - натуральное число"
    if int(length) < 8:
        return "Слишком короткий пароль"
    if int(length) > 127:
        return "Слишком длинный пароль"
    return 0


def sets(repeat, alphabet, type):
    print(type)
    if not set(repeat) & set(Alphabet.lower_case.value) and set(alphabet) & set(type):
        pas = random.SystemRandom().choice(list(set(alphabet) & set(type)))
        return pas
    else:
        return -1


def generate(length, alphabet):
    length = int(length)
    repeat = []
    password = ""
    i = 0
    for _ in range(length):
        pas = -1
        if i == 4:
            i = 0
        while pas == -1 and i <= 3:
            pas = sets(repeat, alphabet, list(Alphabet)[i].value)
            i += 1
        if pas == -1:
            pas = random.SystemRandom().choice(alphabet)
        password += pas
        repeat.append(pas)
    return password