from datetime import datetime, timedelta
import hashlib
import io
import struct


class HashCode:
    def __init__(self,
                 s: str,
                 *,
                 hash_name: str = 'sha512_256',
                 creation_time: datetime = datetime.now(),
                 expiration_in_days: int = 180,
                 iterations: int = 4096,
                 key_len: int = 16):

        self._creation_date: datetime.date = creation_time.isoformat()
        self._expiration_date: datetime.date = (creation_time + timedelta(days=expiration_in_days)).isoformat()

        self._bytes_value: bytes = self.__calculate_salted_hash_code(hash_name, s, iterations, key_len)
        self._hex_value: str = self.__convert_to_hash_value()

    def __calculate_salted_hash_code(self, hash_name: str, s: str, iterations: int, key_len: int):
        password_bytes = bytes(s, 'utf-8')
        salt = bytes(self._expiration_date, 'utf-8')
        return hashlib.pbkdf2_hmac(hash_name=hash_name,
                                   password=password_bytes,
                                   salt=salt,
                                   iterations=iterations,
                                   dklen=key_len)

    def __convert_to_hash_value(self):
        string_io = io.StringIO()
        for i in self._bytes_value:
            a = struct.pack('B', i).hex()
            string_io.write(a)
        return string_io.getvalue()

    @property
    def creation_date(self) -> datetime.date:
        return self._creation_date

    @property
    def expiration_date(self) -> datetime.date:
        return self._expiration_date

    @property
    def bytes_value(self) -> bytes:
        return self._bytes_value

    @property
    def hex_value(self) -> str:
        return self._hex_value
