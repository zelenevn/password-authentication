import random


def generate(alphabet, length):
    if len(alphabet) <= 0:
        raise ValueError('Alphabet must be not empty')
    if length <= 0:
        raise ValueError('Password length must be positive')

    return ''.join(random.choice(alphabet) for _ in range(length))