import random


class PasswordGenerator:
    def password_generation(self, alphabet, length):
        return ''.join(random.choice(alphabet) for _ in range(length))
