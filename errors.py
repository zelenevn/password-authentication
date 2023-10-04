class PASSWORD_LENGTH_ERROR(Exception):
    def __init__(self, *args):
        pass

    def __str__(self):
        return 'Password length must be greater than zero'

class ALPHABET_LENGTH_ERROR(Exception):
    def __init__(self, *args):
        pass

    def __str__(self):
        return 'You have not chosen the password alphabet'

class ALPHABET_AND_PASWORD_LENGTH_ERROR(Exception):
    def __init__(self, *args):
        pass

    def __str__(self):
        return 'You have not chosen the password alphabet and password length must be greater than zero'