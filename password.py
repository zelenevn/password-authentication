import secrets


class Generator:
    def __init__(self):
        pass

    @staticmethod
    def create_new(length, characters):
        return "".join(secrets.choice(characters) for _ in range(length))


