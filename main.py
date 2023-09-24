from generate_password import *


if __name__ == '__main__':
    len_pass, num_selected_groups = interface()
    print("Пароль: " + generate_password(len_pass, num_selected_groups))
