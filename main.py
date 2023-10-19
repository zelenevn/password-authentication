import random
import time
import keyboard as keyboard
import matplotlib.pyplot as plt

characters = "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ"
num_passwords = 1
max_length = int(input('Ведите длину пароля: '))
if max_length < 0:
    raise Exception('Длинна пароля не может быть отрицательна')

passwords = []

for x in range(num_passwords):
    length = max_length
    password = ''.join(random.choice(characters) for y in range(length))
    passwords.append(password)

for password in passwords:
    print(password)

def measure_typing_time(password):
    count = 0
    typing_times = []
    password_length = len(password)

    start = time.time()
    while count < password_length:
        K = keyboard.read_key()
        if keyboard.is_pressed(K):
            count += 1
            typing_times.append(time.time() - start)
            start = time.time()
    return typing_times


def plot_typing_times(typing_times):
    n = len(typing_times)
    x = range(1, n+1)
    y = typing_times

    plt.plot(x, y, 'ro-')
    plt.xlabel("Номер символа")
    plt.ylabel("Время ввода (сек)")
    plt.title("Время ввода символов пароля")
    plt.show()

passw = password
typing_times = measure_typing_time(passw)
plot_typing_times(typing_times)
