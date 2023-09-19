import logical_execution


class Interface:
    func = {}
    choice = "Выбрать вариант:\n1.Выбрать алфавит.\n2.Изменить длину пароля.\n3.Сгенерировать пароль\n"\
                  "4.Ввести пароль\n5.Построить график\n6.Выход"
    alphabet = "Варианты алфавита:\n1.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\n2.abcdefghijklmnopqrstuvwxyz\n"\
              "3.ABCDEFGHIJKLMNOPQRSTUVWXYZ\n4.0-9\n5.0123456789abcdefABCDEF\n6.!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~\n"

    def __init__(self):
        self.func = {
            1: lambda: self.choose_alphabet(),
            2: lambda: self.change_pass_length(),
            3: lambda: self.generate_pass(),
            4: lambda: self.enter_password(),
            5: lambda: self.plot_graph()
        }
        self.exec = logical_execution.LogicalExecution()

    def out(self):
        return print("Invalid value")

    def selection(self):
        while True:
            print(self.choice)
            value = int(input())
            if value > 5:
                break
            self.func.get(value, self.out)()

    def choose_alphabet(self):
        print(self.alphabet)
        print("Выберите алфавит для пароля:" , end="")
        value = list(map(int, input().split()))
        self.exec.choose_alphabet(value)
        return

    def change_pass_length(self):
        print("Enter password length: ", end="")
        value = int(input())
        self.exec.change_pass_length(value)
        return

    def generate_pass(self):
        print(f"Generated password: ", self.exec.get_last_pass())
        return

    def enter_password(self):
        print("Enter password: ", end="")
        self.exec.enter_password()
        return

    def plot_graph(self):
        self.exec.plot_graph()
        return
