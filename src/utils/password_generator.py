import random


class PasswordGenerator:
    def __init__(self, alphabet: str, length: int):
        if length < 6:
            raise ValueError('The password must be at least 6 characters long!')
        if len(alphabet) < 30:
            raise ValueError('The length of the alphabet is at least 30 characters!')
        lst = list(alphabet)
        self._value = ''.join([random.choice(lst) for _ in range(length)])

        if getattr(self, '_value', None) is None:
            raise ValueError('An unexpected error has occurred!')

    @property
    def value(self) -> str:
        return self._value
