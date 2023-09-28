from datetime import datetime, timedelta
import hashlib
import io
import struct


def _calculate_salted_hash_code(hash_name: str, s: str, salt: datetime.date, iterations: int, key_len: int):
    password_bytes = bytes(s, 'utf-8')
    salt = bytes(salt, 'utf-8')
    return hashlib.pbkdf2_hmac(hash_name=hash_name,
                               password=password_bytes,
                               salt=salt,
                               iterations=iterations,
                               dklen=key_len)


def _convert_to_hash_value(bytes_value: bytes):
    string_io = io.StringIO()
    for i in bytes_value:
        a = struct.pack('B', i).hex()
        string_io.write(a)
    return string_io.getvalue()


class HashCode:
    def __init__(self,
                 s: str,
                 salt: datetime.date,
                 *,
                 hash_name: str = 'sha512_256',
                 iterations: int = 4096,
                 key_len: int = 16):

        self._bytes_value: bytes = _calculate_salted_hash_code(hash_name, s, salt, iterations, key_len)
        self._hex_value: str = _convert_to_hash_value(self._bytes_value)

    @property
    def bytes_value(self) -> bytes:
        return self._bytes_value

    @property
    def hex_value(self) -> str:
        return self._hex_value
