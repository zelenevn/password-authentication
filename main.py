
import secrets
import string
import time
import matplotlib.pyplot as plt

import keyboard


def generate_password(alphabet, length):
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def choose_alphabet():
    alphabet = ''
    chains_alphabet = {"A-Z: ": string.ascii_uppercase,
              "a-z: ": string.ascii_lowercase,
              'а-я:':'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
              'А-Я:': 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
              "0-9: ": string.digits, "!@#: ": string.punctuation}

    for c in chains_alphabet.keys():
        if input(c) in ["", "+"]:
            alphabet += chains_alphabet[c]
    return alphabet

def count_key_overlaps(password):
    count = 0
    times = []
    while count <= len(password):
        K = keyboard.read_key()
        if keyboard.is_pressed(K):
            count += 1
            times.append(time.time())

    return times

alphabet = choose_alphabet()
length = int(input("L = "))
print("alphabet:", alphabet)
password = generate_password(alphabet, length)
print("password: ", password)




print("start test")
keys = count_key_overlaps(password)

plt.title('Задержки между нажатиями, ms')
plt.plot(
    ['{}-{}'.format(i,i+1) for i in range(len(keys)-1)],
    [(keys[i+1]-keys[i])*1000 for i in range(len(keys)-1)],
    'ro')
plt.show()


