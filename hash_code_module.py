from datetime import datetime, timedelta
import hashlib
import io
import logging
import struct

logging.basicConfig(filename='logfile.log',
                    encoding='cp1251',
                    filemode='a',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')


class HashCode:
    def __init__(self,
                 s: str,
                 *,
                 hash_name: str = 'sha512_256',
                 creation_time: datetime = datetime.now(),
                 expiration_in_days: int = 180,
                 iterations: int = 4096,
                 key_len: int = 32):

        self._creation_date = creation_time.strftime(f'%Y-%m-%d')
        self._expiration_date = (creation_time + timedelta(days=expiration_in_days)).strftime(f'%Y-%m-%d')

        self.__calculate_salted_hash_code(hash_name, s, iterations, key_len)
        self.__convert_to_hash_value()

        logging.info(f'Пароль был успешно хеширован!')

    def __calculate_salted_hash_code(self, hash_name: str, s: str, iterations: int, key_len: int):
        password_bytes = bytes(s, 'utf-8')
        salt = bytes(self._expiration_date, 'utf-8')
        self._hash_value: bytes = hashlib.pbkdf2_hmac(hash_name=hash_name,
                                                      password=password_bytes,
                                                      salt=salt,
                                                      iterations=iterations,
                                                      dklen=key_len)

    def __convert_to_hash_value(self):
        string_io = io.StringIO()
        for i in self._hash_value:
            a = struct.pack('B', i).hex()
            string_io.write(a)
        self._hex_hash_value = string_io.getvalue()

    @property
    def creation_date(self) -> str:
        return self._creation_date

    @property
    def expiration_date(self) -> str:
        return self._expiration_date

    @property
    def hash_value(self) -> bytes:
        return self._hash_value

    @property
    def hex_hash_value(self) -> str:
        return self._hex_hash_value
