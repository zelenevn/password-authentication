
import string

import coefficient_calculator
import password

def get_alphabet():
    alphabet = ''
    chains = {"A-Z: ": string.ascii_uppercase, "a-z: ": string.ascii_lowercase, "0-9: ":  string.digits, "!@#: ": string.punctuation}
    for c in chains.keys():
        if input(c) in ["", "+"]:
            alphabet += chains[c]
    return alphabet

alphabet = get_alphabet()
length = int(input("L = "))

V = 1000
T = 30
print("alphabet:", alphabet)
print(password.generate(alphabet, length))
print(coefficient_calculator.P(alphabet, length, V, T))





