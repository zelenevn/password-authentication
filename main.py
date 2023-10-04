from password_generator import PasswordGenerator

def main():
    print("ГЕНЕРАТОР ПАРОЛЕЙ")
    try:
        password_length = int(input("Введите длину пароля (не менее 6 символов): "))
        if password_length < 6:
            print("Ошибка: Длина пароля должна быть не менее 6 символов")
            exit(1)
    except ValueError:
        print("Ошибка: Пожалуйста, введите целое число")
        exit(1)

    print("Выберите группы символов для пароля:")
    print("1. Строчные буквы")
    print("2. Заглавные буквы")
    print("3. Цифры")
    print("4. Специальные символы")

    selected_groups = input("Введите номера выбранных групп символов: ")
    valid_groups = set("1234")
    if not selected_groups or not set(selected_groups).issubset(valid_groups):
        print("Ошибка: Выберите группу символов (от 1 до 4)")
        exit(1)

    if not selected_groups:
        selected_groups = "1234"  # Если пользователь не выбрал группы, используем все группы по умолчанию

    generator = PasswordGenerator(password_length)

    password = generator.generate_password(selected_groups)
    print("Сгенерированный пароль:", password)

    max_t = int(input("Введите максимальный срок действия пароля (в днях): "))
    cracking_speed = int(input("Введите скорость перебора паролей (попыток в минуту): "))
    probability = generator.durability(max_t, cracking_speed)
    print(f"Вероятность подбора пароля за {max_t} дней при скорости {cracking_speed} попыток/мин: {probability:.20f}")


if __name__ == "__main__":
    main()
