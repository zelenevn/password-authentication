import random


class PasswordGenerator:
    def __init__(self, alphabet: str, length: int):

        if length < 6:
            raise ValueError('Длина пароля должна быть не менее 6 символов!')
        if len(alphabet) < 30:
            raise ValueError('Мощность алфавита пароля должна быть не менее 30 символов!')

        lst = list(alphabet)
        self._value = ''.join([random.choice(lst) for _ in range(length)])

        if getattr(self, '_value', None) is None:
            raise ValueError('Произошла непредвиденная ошибка!')

    @property
    def value(self) -> str:
        return self._value
