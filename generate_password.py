import secrets as s
import string

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
PUNCTUATION = string.punctuation

ALL_SYMBOLS = [LOWERCASE, UPPERCASE, DIGITS, PUNCTUATION]


def create_dictionary(selected: list) -> list:
    list_dictionary = []
    for choice in selected:
        list_dictionary.append(ALL_SYMBOLS[choice])
    return list_dictionary


def make_groups_distribution(count_groups: int, len_pass: int) -> list:
    groups_distribution = list()

    for i in range(count_groups, 1, -1):
        num_symbol = s.SystemRandom().randint(
            1,
            len_pass - i + 1 - sum(groups_distribution)
        )
        groups_distribution.append(num_symbol)
    groups_distribution.append(len_pass - sum(groups_distribution))
    return groups_distribution


def generate_password(len_pass: int, num_selected_groups: list):
    groups_distribution = make_groups_distribution(
        count_groups=len(num_selected_groups),
        len_pass=len_pass)

    parts_password = list()

    for i, num in enumerate(num_selected_groups):
        count = groups_distribution[i]
        parts_password.append(
            ''.join([s.choice(ALL_SYMBOLS[num]) for _ in range(count)])
        )

    pre_ready_password = ''.join(parts_password)

    return ''.join(
        s.SystemRandom().sample(
            pre_ready_password, k=len(pre_ready_password)
        )
    )


for i in range(10):
    print(generate_password(len_pass=10, num_selected_groups=[1, 2, 3]))
