import io
from datetime import datetime, timedelta
import hashlib
import logging
import struct
import random

logging.basicConfig(filename='logfile.log',
                    encoding='cp1251',
                    filemode='a',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')


class Generator:
    @classmethod
    def generate_password(cls, alphabet: str, length: int) -> str:
        try:
            if length < 6:
                raise ValueError('Длина пароля должна быть не менее 6 символов!')
            if len(alphabet) < 30:
                raise ValueError('Алфавит пароля не менее 30 символов!')

            lst = list(alphabet)
            password = ''.join([random.choice(lst) for _ in range(length)])
        except ValueError as e:
            logging.exception(e)
        else:
            return password


class Hashing:
    hash_name: str = 'sha512_256'
    expiration_in_days: int = 180
    iterations: int = 4096
    key_len: int = 32

    @classmethod
    def hash_with_salt(cls,
                       value: str,
                       flag_return_hex: bool,
                       creation_time: datetime = None,
                       expiration_time: datetime = None) -> (str | bytes, datetime, datetime):

        password_bytes = bytes(value, 'utf-8')

        if not (creation_time and expiration_time):
            creation_time = datetime.now().strftime(f'%Y-%m-%d')
            expiration_time = (datetime.now() + timedelta(days=cls.expiration_in_days)).strftime(f'%Y-%m-%d')

        salt = bytes(expiration_time, 'utf-8')

        h: bytes = hashlib.pbkdf2_hmac(hash_name=cls.hash_name,
                                       password=password_bytes,
                                       salt=salt,
                                       iterations=cls.iterations,
                                       dklen=cls.key_len)
        hashed_value = h
        if flag_return_hex:
            string_io = io.StringIO()
            for i in h:
                a = struct.pack('B', i).hex()
                string_io.write(a)
            hashed_value = string_io.getvalue()
        logging.info(f'Пароль был успешно хеширован!')
        return hashed_value, creation_time, expiration_time


class AccessCode:
    def __init__(self, alphabet: str, length: int):

        self._value = Generator.generate_password(alphabet, length)
        logging.info('Пароль закончил генерацию!')

        try:
            if getattr(self, '_value', None) is None:
                raise ValueError('Несуществующий пароль не может быть хеширован!')
        except Exception as e:
            logging.exception(e)
        else:
            self._hashed_value, self._creation_date, self._expiration_date = Hashing.hash_with_salt(self.value, True)

    @property
    def value(self) -> str:
        return self._value

    @property
    def hashed_value(self) -> str:
        print(self._hashed_value)
        return self._hashed_value

    @property
    def creation_date(self) -> str:
        return self._creation_date

    @property
    def expiration_date(self) -> str:
        return self._expiration_date
