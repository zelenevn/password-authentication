import pytest
from generator import Generator
from logical_execution import LogicalExecution

check = lambda a: True if a in "0123456789abcdefABCDEF" else False
def test_generator():
    gen = Generator()
    assert type(gen.generate_password()) == type('')
    assert len(gen.generate_password()) == 8
    assert all([check(x) for x in gen.generate_password()]) == True


def test_le_get_alphabet():
    le = LogicalExecution()
    assert le.get_alphabet(1) == "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert le.get_alphabet(2) == "abcdefghijklmnopqrstuvwxyz"
    assert le.get_alphabet(3) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert le.get_alphabet(4) == "0123456789"
    assert le.get_alphabet(5) == "0123456789abcdefABCDEF"
    assert le.get_alphabet(6) == "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    with pytest.raises(Exception) as error:
        le.get_alphabet(7)
    assert "Wrong option" == error.value.args[0]



if __name__ == '__main__':
    pytest.main()
