from password_generator import PasswordGenerator


def main():
    print("Генератор паролей")
    print("===================")

    try:
        password_generator = PasswordGenerator()
        password_generator.length = int(input("Введите длину пароля: "))

        print("Выберите группы символов для пароля:")
        print("1. Строчные буквы")
        print("2. Заглавные буквы")
        print("3. Цифры")
        print("4. Специальные символы")
        selected_alphabets = [int(x) for x in input("Введите номера выбранных групп символов через пробел: ").split()]
        password_generator.selected_alphabets = selected_alphabets

        password, complexity = password_generator.generate_password()
        print(f"Сгенерированный пароль: {password}")
        print(f"Сложность пароля: {complexity}")
    except ValueError:
        print("Некорректная длина пароля или количество выбранных групп символов.")


if __name__ == "__main__":
    main()
