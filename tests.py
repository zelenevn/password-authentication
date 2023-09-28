import unittest
import re
from itertools import combinations
from generate_password import generate_password, ALL_SYMBOLS


class TestPassword(unittest.TestCase):

    def test_len(self):
        for i in range(7, 20):
            self.assertTrue(
                len(generate_password(i, [0, 1, 2, 3])) > 6
            )

        for i in range(1, 7):
            with self.assertRaises(ValueError):
                generate_password(i, [0, 1, 2, 3])

    def test_len_alphabet(self):
        num_groups = [0, 1, 2, 3]

        for i in range(3, 5):

            for comb in combinations(num_groups, i):
                num_selected_groups = comb
                now_alphabet = ''.join([ALL_SYMBOLS[i] for i in num_selected_groups])

                self.assertTrue(
                    len(now_alphabet) > 30
                )

    def test_occurrence_all_alphabets(self):
        num_groups = [0, 1, 2, 3]
        for i in range(3, 5):
            for comb in combinations(num_groups, i):
                password = generate_password(10, comb)
                match_letter = re.search('[a-zA-Z]', password)

                self.assertTrue(
                    match_letter is not None
                )


if __name__ == '__main__':
    unittest.main()
