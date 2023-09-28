from pydantic import ValidationError
from src.auth.router import register_user, identify_user
from src.utils.ascii_alphabet import assemble_alphabet
from src.utils.key_listener import data_collection_for_input
from src.utils.password_generator import PasswordGenerator


if __name__ == '__main__':
    while True:
        registered = input('Are you registered? (y/n): ')
        if registered.lower() == 'y':
            username = input('Enter your username: ')
            print('Enter your password: ')
            password, intervals = data_collection_for_input()
            try:
                print(identify_user(username=username, password=password, intervals=intervals))
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
            print(alphabet)

            length = int(input('Enter length: '))

            password = PasswordGenerator(alphabet, length).value
            print(f'Your password:\n{password}')

            try:
                response = register_user(username=username, password=password)
                # Создаем нового пользователя в базе данных или выполняем другие действия
            except ValidationError as e:
                print(e)
        elif registered.lower() == 'q':
            break
        else:
            print('Invalid input. Please enter y, n or q.')
