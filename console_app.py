import logic_service


class ConsoleApp:
    def __init__(self):
        self.ls = logic_service.LogicService()

    def select_action(self):
        print("Выберите:\n1. Сгенерировать пароль\n2. Ввести пароль\n3. Вывести число наложений\nВыход")
        var = int(input())
        match var:
            case 1:  # генерация пароля
                self.generation_password()
            case 2:  # ввод пароля
                self.input_password()
            case 3:  # вывести число наложений 3-его типа
                self.output_num_overdubs()
            case default:
                return False
        return True

    def generation_password(self):
        self.ls.generate_password()
        return

    def input_password(self):
        self.ls.input_password()
        return

    def output_num_overdubs(self):
        self.ls.get_num()
        return

    def console_app(self):
        while True:
            if not self.select_action():
                break
        return
