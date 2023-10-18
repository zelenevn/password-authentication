import string
import generator
import keyboard


class LogicService:
    chars = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    input_sequence = []

    def __init__(self):
        self.generator = generator.PasswordGenerator()
        pass

    def generate_password(self):
        print("Выберите парольный алфавит(+, -):\n"
              "Добавить a-z?\n"
              "Добавить A-Z?\n"
              "Добавить 0-9?\n"
              "Добавить спец. символы?")

        values = input()
        alphabet = ""
        for i in range(len(values)):
            if values[i] == "+":
                alphabet += self.chars[i]

        print("Укажиет длину пароля: ", end="")
        length = int(input())
        print(f"Сгенерированный пароль - ", self.generator.password_generation(alphabet, length))
        return

    def input_password(self):
        self.input_sequence = []
        print("Введите пароль: ", end="")
        keyboard.hook(self.get_sequence)
        keyboard.wait("enter")
        keyboard.unhook(self.get_sequence)
        input()
        return

    def get_sequence(self, e):
        if e.name == "enter":
            return
        if e.event_type == "down":
            self.input_sequence.append(e.name)
        elif e.event_type == "up":
            self.input_sequence.append(e.name)

    def get_num(self):
        print(f"Количесвто наложений - ", self.get_index(self.input_sequence))
        return

    def get_index(self, arr):
        print(arr)
        sum = 0
        start = 0
        end = arr[start + 1:].index(arr[start]) + 1

        while True:
            if end - start > 2:
                sum += self.get_count(arr[start + 1:end])
            if end == len(arr) - 1 or start >= end:
                break
            start = end + 1
            if start != len(arr) and arr[start] in arr[start + 1:]:
                end = start + arr[start + 1:].index(arr[start]) + 1
            else:
                end = start+1
        return sum

    def get_count(self, arr):
        count = 0
        pars = set()
        for i in range(len(arr)):
            if arr[i] in pars:
                pars.remove(arr[i])
                count += 1
            else:
                pars.add(arr[i])
        return count
