import random
import time
import matplotlib.pyplot as plt

characters = "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ"
num_passwords = 1
max_length = int(input('Ведите длину пароля: '))
if max_length < 0:
    raise Exception('Длинна пароля неверна')

passwords = []

for x in range(num_passwords):
    length = max_length
    password = ''.join(random.choice(characters) for y in range(length))
    passwords.append(password)

for password in passwords:
    print(password)

def measure_typing_time(password):
    typing_times = []
    password_length = len(password)

    for i in range(password_length):
        start_time = time.time()
        user_input = input("Введите символ пароля: ")
        end_time = time.time()
        typing_time = end_time - start_time

        if user_input != password[i]:
            print("Неверно введен символ пароля")
            return

        typing_times.append(typing_time)

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
