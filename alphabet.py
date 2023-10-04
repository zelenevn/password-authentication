import string

chains_alphabet = {"A-Z: ": string.ascii_uppercase,
                   "a-z: ": string.ascii_lowercase,
                   'а-я:': 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                   'А-Я:': 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
                   "0-9: ": string.digits, "!@#: ": string.punctuation}
