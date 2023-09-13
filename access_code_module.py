import logging
from generator_module import Generator
from hash_code_module import HashCode

logging.basicConfig(filename='logfile.log',
                    encoding='cp1251',
                    filemode='a',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')


class AccessCode:
    def __init__(self, alphabet: str, length: int):
        try:
            self._value = Generator.generate_access_code(alphabet, length)
            logging.info('Пароль закончил генерацию!')

            if getattr(self, '_value', None) is None:
                raise ValueError('Несуществующий пароль не может быть хеширован!')
            self._hash_code = HashCode(self._value)
        except Exception as e:
            logging.exception(e)

    @property
    def value(self) -> str:
        return self._value

    @property
    def hash_code(self) -> HashCode:
        return self._hash_code
