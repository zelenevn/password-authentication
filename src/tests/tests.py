import random
import unittest
from sqlalchemy import delete
from src.auth.models import User
from src.auth.router import register_user, identify_user
from src.database import session_maker
from src.utils.ascii_alphabet import assemble_alphabet
from src.utils.password_generator import PasswordGenerator
import json
import os

filename: str = 'users.json'


def generate_users_to_json():
    users_data = []
    for count, i in enumerate(range(6, 10)):
        password_obj = PasswordGenerator(assemble_alphabet(('LOWER_CASE', 'UPPER_CASE')), 6)
        user_data = {}
        user_data.update({'username': f'test_{count}'})
        user_data.update({'password': password_obj.value})
        user_data.update({'alphabet': password_obj.alphabet})
        user_data.update({'intervals':
                              [[random.uniform(0, 1) for _ in range(len(password_obj.value) - 1)] for _ in range(i)]})
        user_data.update({'holdings_time':
                              [[random.uniform(0, 1) for _ in range(len(password_obj.value))] for _ in range(i)]})

        users_data.append(user_data)

    with open(f'{os.getcwd()}/{filename}', 'w') as file:
        file.write(json.dumps(users_data, indent=4))


class TestUser(unittest.TestCase):
    def setUp(self):
        generate_users_to_json()
        with open(filename, 'r') as f:
            self.users_data = json.load(f)

    def test_registration_and_identification(self):
        for user_data in self.users_data:
            result = register_user(**user_data)
            print(f"Registration for {user_data.get('username')}: {result}")
            self.assertEqual('success', result['status'])

        for user_data in self.users_data:
            user_attempt = {'username': user_data['username'],
                            'password': user_data['password'],
                            'intervals': (user_data['intervals'])[0],
                            'holdings_time': (user_data['holdings_time'])[0]}
            result = identify_user(**user_attempt)
            print(f"Identification for {user_data.get('username')}: {result}")
            self.assertEqual('permit', result['status'])

    def tearDown(self):
        session = session_maker()
        try:
            for user_data in self.users_data:
                stmt = delete(User).where(User.username == str(user_data['username']).strip())
                session.execute(stmt)
                session.commit()
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()


if __name__ == '__main__':
    unittest.main()
