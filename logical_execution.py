import keyboard
import time
import generator
import matplotlib.pyplot as plt
import numpy as np
import string


class LogicalExecution:
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
        6: lambda: string.punctuation,  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    }
    down = "down"
    up = "up"

    def choose_alphabet(self, value):
        chars = []
        for i in range(len(value)):
            chars += self.get_alphabet(value[i])
        self.generator.set_chars(chars)
        return

    def wrong_alphabet(self):
        raise Exception("Wrong option")

    def get_alphabet(self, value):
        return self.variants.get(value, self.wrong_alphabet)()

    def change_pass_length(self, value):
        self.generator.set_length(value)
        return

    def get_last_pass(self):
        self.last_pass = self.generator.generate_password()
        return self.last_pass

    def enter_password(self):
        keyboard.hook(self.get_time)
        keyboard.wait("enter")
        self.time_periods.pop()
        for i in range(0, len(self.time_periods), 2):
            self.result_last_pass.append(self.time_periods[i + 1] - self.time_periods[i])
        input()
        return

    def get_time(self, e):
        if e.event_type == self.down:
            # start timer
            self.time_periods.append(time.time())
        elif e.event_type == self.up:
            # end timer
            self.time_periods.append(time.time())

    def plot_graph(self):
        y = [i + 1 for i in range(len(self.result_last_pass))]
        plt.bar(y, self.result_last_pass, edgecolor='black', align='center')
        plt.xticks(np.arange(min(y), max(y) + 1, 1.0))
        plt.show()
        return
