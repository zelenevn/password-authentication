import keyboard
import time
import generator
import matplotlib.pyplot as plt
import numpy as np
import string


class Execute:
    func = {}
    generator = generator.Generator()
    last_pass = ""
    result_last_pass = []
    time_periods = []
    variants = {
        1: lambda: string.ascii_letters,  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
        2: lambda: string.ascii_lowercase,  # abcdefghijklmnopqrstuvwxyz
        3: lambda: string.ascii_uppercase,  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
        4: lambda: string.digits,  # 0-9
        5: lambda: string.hexdigits,  # 0123456789abcdefABCDEF
        6: lambda: string.punctuation,  # !"#$%&'()*+,-./:;?@[\]^_`{|}~
    }

    def __init__(self):
        self.func = {
            1: lambda: self.choose_alphabet(),
            2: lambda: self.change_pass_length(),
            3: lambda: self.generate_pass(),
            4: lambda: self.enter_password(),
            5: lambda: self.plot_graph()
        }
        # self.values = []

    def out(self):
        return print("Invalid value")

    def selection(self):
        while True:
            print("Выбрать вариант:\n"
                  "1.Выбрать алфавит.\n"
                  "2.Изменить длину пароля.\n"
                  "3.Сгенерировать пароль\n"
                  "4.Ввести пароль\n"
                  "5.Построить график\n"
                  "6.Выход")
            value = int(input())
            if value > 5:
                break
            self.func.get(value, self.out)()

    def choose_alphabet(self):
        print("Варианты алфавита:\n"
              "1.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\n"
              "2.abcdefghijklmnopqrstuvwxyz\n"
              "3.ABCDEFGHIJKLMNOPQRSTUVWXYZ\n"
              "4.0-9\n"
              "5.0123456789abcdefABCDEF\n"
              "6.!\"#$%&'()*+,-./:;?@[\]^_`{|}~")
        print("Выберите алфавит для пароля: ", end="")
        value = list(map(int, input().split()))
        chars = []
        for i in range(len(value)):
            chars += self.get_alphabet(value[i])
        self.generator.set_chars(chars)
        return

    def default_alphabet(self):
        return print("Wrong option!!!")

    def get_alphabet(self, value):
        return self.variants.get(value, self.default_alphabet)()

    def change_pass_length(self):
        print("Enter password length:", end=" ")
        value = int(input())
        self.generator.set_length(value)
        return

    def generate_pass(self):
        self.last_pass = self.generator.generate_password()
        print(f"Generated password: ", self.last_pass)
        return

    def enter_password(self):
        print("Enter password:", end=" ")
        keyboard.hook(self.get_time)
        keyboard.wait("enter")
        self.time_periods.pop()
        for i in range(0, len(self.time_periods), 2):
            self.result_last_pass.append(self.time_periods[i + 1] - self.time_periods[i])
        input()
        return

    def get_time(self, e):
        if e.event_type == 'down':
            # start timer
            self.time_periods.append(time.time())
        elif e.event_type == 'up':
            # end timer
            self.time_periods.append(time.time())

    def plot_graph(self):
        y = [i + 1 for i in range(len(self.result_last_pass))]
        plt.bar(y, self.result_last_pass, edgecolor='black', align='center')
        plt.xticks(np.arange(min(y), max(y) + 1, 1.0))
        plt.show()
        return
