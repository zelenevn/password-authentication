import random


class PasswordGenerator:
    def __init__(self, alphabet: str, length: int):
        self._alphabet = alphabet
        self._value = ''.join([random.choice(list(alphabet)) for _ in range(length)])

        if getattr(self, '_value', None) is None:
            raise ValueError('An unexpected error has occurred!')

    @property
    def alphabet(self):
        return self._alphabet

    @property
    def value(self) -> str:
        return self._value
