import random


class PasswordGenerator:
    def __init__(self, alphabet: str, length: int):
        lst = list(alphabet)
        self._value = ''.join([random.choice(lst) for _ in range(length)])

        if getattr(self, '_value', None) is None:
            raise ValueError('Произошла непредвиденная ошибка!')

    @property
    def value(self) -> str:
        return self._value
