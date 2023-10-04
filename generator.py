import secrets

import errors


class Generator:
    def __init__(self, alphabet, length):
        self.__alphabet = alphabet
        self.__length = length

    def get_password(self):
        if len(self.__alphabet) <= 0 and self.__length <= 0:
            return errors.ALPHABET_AND_PASWORD_LENGTH_ERROR
        if len(self.__alphabet) <= 0:
            return errors.ALPHABET_LENGTH_ERROR
        if self.__length <= 0:
            return errors.PASSWORD_LENGTH_ERROR

        return ''.join(secrets.choice(self.__alphabet) for _ in range(self.__length))

    def set_alphabet(self, alphabet:str):
        self.__alphabet = alphabet

    def set_length(self, length):
        self.__length = length

    def get_alphabet(self)->str:
        return self.__alphabet

    def get_length(self)->int:
        return self.__length