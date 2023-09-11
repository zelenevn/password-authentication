import functools
import io
import logging
from enum import Enum
from collections.abc import Iterable
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

logging.basicConfig(filename='logfile.log',
                    encoding='cp1251',
                    filemode='a',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')


Alphabet = Enum('Alphabet', [('LOWER_CASE', ascii_lowercase),
                             ('UPPER_CASE', ascii_uppercase),
                             ('DIGITS', digits),
                             ('PUNCTUATION', punctuation)])


@functools.lru_cache(maxsize=None)
def assemble_alphabet(chosen_alphabets: Iterable) -> str | None:
    try:
        string_io = io.StringIO()
        for name, member in Alphabet.__members__.items():
            if name in chosen_alphabets:
                string_io.write(member.value)
        if not bool(string_io.getvalue()):
            raise ValueError('Не был выбран какой-нибудь алфавит!')
        logging.info('Алфавит был успешно составлен!')
        return string_io.getvalue()
    except ValueError as e:
        logging.error(f'Ошибка в assemble_alphabet! {e}')
        return None
