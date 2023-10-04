
from alphabet import chains_alphabet


class Console_controller:
    @staticmethod
    def choose_alphabet():
        alphabet = ''
        for c in chains_alphabet.keys():
            if input(c) in ["", "+"]:
                alphabet += chains_alphabet[c]
        return alphabet

    @staticmethod
    def get_size():
        return int(input("L = "))
