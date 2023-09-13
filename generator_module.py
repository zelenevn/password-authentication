import logging
import random

logging.basicConfig(filename='logfile.log',
                    encoding='cp1251',
                    filemode='a',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')


class Generator:
    @staticmethod
    def generate_access_code(alphabet: str, length: int) -> str | None:
        try:
            if length < 6:
                raise ValueError('Длина кода доступа должна быть не менее 6 символов!')
            if len(alphabet) < 30:
                raise ValueError('Мощность алфавита кода доступа должна быть не менее 30 символов!')

            lst = list(alphabet)
            password = ''.join([random.choice(lst) for _ in range(length)])
            return password
        except ValueError as e:
            logging.exception(f'Ошибка в Generator.generate_password()! {e}')
            return None
