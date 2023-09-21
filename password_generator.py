import random


class Password_generator:
    def __init__(self, alphabet:str, length:int):
        self.__alphabet = alphabet
        self.__length = length
    def generate(self):
        return ''.join(random.choice(self.__alphabet) for _ in range(self.__length))

    def set_alphabet(self, alphabet:str):
        self.__alphabet = alphabet
    def set_length(self, length):
        self.__length = length

    def get_alphabet(self)->str:
        return self.__alphabet

    def get_length(self)->int:
        return self.__length

