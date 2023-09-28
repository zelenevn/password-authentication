import functools
import io
from enum import Enum
from collections.abc import Iterable
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


Alphabet = Enum('Alphabet', [('LOWER_CASE', ascii_lowercase),
                             ('UPPER_CASE', ascii_uppercase),
                             ('DIGITS', digits),
                             ('PUNCTUATION', punctuation)])


@functools.lru_cache(maxsize=None)
def assemble_alphabet(alphabets: Iterable) -> str | None:
    string_io = io.StringIO()
    for name in alphabets:
        try:
            value = Alphabet.__members__.get(name, None).value
        except AttributeError:
            raise AttributeError(f'Алфавита {name} не существует!')
        string_io.write(value)
    if not bool(string_io.getvalue()):
        raise ValueError('Не был выбран какой-нибудь алфавит!')

    return string_io.getvalue()