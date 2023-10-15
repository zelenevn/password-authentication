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
        return "Ошибка ввода длины алфавита. Длина алфавита - натуральное число"
    if int(length) < 0 or int(length) > 94:
        return "Неверная длина алфавита"
    return 0


def generate(length):
    length = int(length)
    alphabet = ''
    repeat = []
    i = 0

    while i < length:
        type_of_elem = random.SystemRandom().choice(list(Alphabet))
        elem = random.choice(type_of_elem.value)
        if elem not in repeat:
            alphabet += elem
            repeat.append(elem)
            i += 1
    return alphabet