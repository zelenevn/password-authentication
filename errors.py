class PASSWORD_LENGTH_ERROR(Exception):
    def __init__(self, *args):
        pass

    def __str__(self):
        return 'Длина пароля должна быть больше нуля'

class ALPHABET_LENGTH_ERROR(Exception):
    def __init__(self, *args):
        pass

    def __str__(self):
        return 'Вы не выбрали алфавит'

class ALPHABET_AND_PASWORD_LENGTH_ERROR(Exception):
    def __init__(self, *args):
        pass

    def __str__(self):
        return 'Вы не выбрали алфавит и длина пароля должна быть больше нуля'