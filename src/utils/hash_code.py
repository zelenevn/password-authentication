from datetime import datetime
import hashlib
import io
import struct


class HashCode:
    hash_name = 'sha512_256'
    iterations = 4096
    key_len = 16

    def __init__(self, *, s: str, salt: str):
        s_bytes = s.encode('utf-8')
        s_salt = salt.encode('utf-8')

        self._bytes_value = self._calculate_salted_hash_code(s_bytes, s_salt)
        self._hex_value = self._convert_to_hash_value()

    @property
    def bytes_value(self):
        return self._bytes_value

    @property
    def hex_value(self):
        return self._hex_value

    def _calculate_salted_hash_code(self, s: bytes, salt: bytes):
        return hashlib.pbkdf2_hmac(
            hash_name=self.hash_name,
            password=s,
            salt=salt,
            iterations=self.iterations,
            dklen=self.key_len
        )

    def _convert_to_hash_value(self):
        string_io = io.StringIO()
        for i in self.bytes_value:
            a = struct.pack('B', i).hex()
            string_io.write(a)
        return string_io.getvalue()
