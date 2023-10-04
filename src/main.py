from pydantic import ValidationError
from src.auth.router import register_user, identify_user
from src.drawing.piecewise_constant_function import draw
from src.utils.ascii_alphabet import assemble_alphabet
from src.utils.key_listener import collect_data_for_input
from src.utils.password_generator import PasswordGenerator


def main():
    while True:
        registered = input('Are you registered? (y/n): ')
        if registered.lower() == 'y':
            username = input('Enter your username: ')
            print('Enter your password: ')
            password, intervals, holdings_time = collect_data_for_input()
            draw(intervals, holdings_time)
            try:
                response = identify_user(username=username,
                                         password=password,
                                         intervals=intervals,
                                         holdings_time=holdings_time)
                print(response)
            except ValidationError as e:
                print(e)

        elif registered.lower() == 'n':
            username = input('Choose a username: ')

            dic: dict = {1: 'LOWER_CASE', 2: 'UPPER_CASE', 3: 'DIGITS', 4: 'PUNCTUATION'}
            chosen_alphabets = input('Choose alphabets for generation your password using space\n'
                                     '"1" - LOWER_CASE\n'
                                     '"2" - UPPER_CASE\n'
                                     '"3" - DIGITS\n'
                                     '"4" - PUNCTUATION\n'
                                     '>> ')
            chosen_alphabets = tuple(set([dic.get(x, None) for x in list(map(int, chosen_alphabets.split()))]))
            alphabet = assemble_alphabet(chosen_alphabets)

            length = int(input('Enter length: '))

            password_obj = PasswordGenerator(alphabet, length)
            print(f'Your password:\n{password_obj.value}')

            while True:
                answer = input('Would you like to save your password? (y/n) ')
                if answer.lower() == 'y':
                    with open('password.txt', mode='w', encoding='utf-8') as file:
                        file.write(password_obj.value)
                    break
                elif answer.lower() == 'n':
                    break

            intervals = []
            holdings_time = []

            i = 0
            n = 3
            while i < n:
                print(f'Repeat your password ({n - i} times left): ')
                try:
                    password_i, intervals_i, holdings_time_i = collect_data_for_input()
                    if password_obj.value == password_i:
                        intervals.append(intervals_i)
                        holdings_time.append(holdings_time_i)
                        i += 1
                    else:
                        raise ValueError('Invalid password! Try one more time!')
                except ValueError as e:
                    print(e)
                    continue

            try:
                response = register_user(username=username,
                                         password=password_obj.value,
                                         alphabet=password_obj.alphabet,
                                         intervals=intervals,
                                         holdings_time=holdings_time)
                print(response)
                # Создаем нового пользователя в базе данных или выполняем другие действия
            except ValidationError as e:
                print(e)
        elif registered.lower() == 'q':
            break
        else:
            print('Invalid input. Please enter y, n or q.')


if __name__ == '__main__':
    main()
