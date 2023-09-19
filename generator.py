import random
import string


class Generator:
    def __init__(self):
        self.alphabet = string.hexdigits
        self.length = 8

    def generate_password(self):
        return ''.join(random.choice(self.alphabet) for _ in range(self.length))

    def set_chars(self, chars):
        self.alphabet = chars

    def set_length(self, value):
        self.length = value
