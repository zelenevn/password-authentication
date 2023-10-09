# decorators.py
import functools
import math


def validate_password(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        password = func(*args, **kwargs)
        # print(1, password, type(password))

        count_numbers_password = sum(c.isdigit() for c in password)  # Кол-во цифр в пароле
        count_lower_password = sum(c.islower() for c in password)  # Кол-во букв нижнего регистра в пароле
        count_upper_password = sum(c.isupper() for c in password)  # Кол-во букв верхнего регистра в пароле
        count_letters_password = count_lower_password + count_upper_password  # Кол-во букв в пароле
        percent = 0.15  # Процент (длины пароля)
        decrease_scales = 0.11  # Уменьшение веса
        change_scales = 0.61  # Изначальный вес

        # - Длина пароля не менее 6 символов;
        if len(password) < 6:
            return "Длина пароля должна быть не менее 6 символов"

        # - Пароль должен включать min (1 верхний регистр, 1 цифру, 4 буквы)
        if count_numbers_password < 1:
            return "Пароль должен содержать цифры"
        if count_upper_password < 1:
            return "Пароль должен содержать заглавные буквы"
        if count_letters_password < 4:
            return "Пароль должен содержать больше букв"

        # print(f"Длина: {len(password)}")
        # print(f"Уникальных символов: {len(set(password))}")
        # print(f"Максимальный вес: {math.ceil(len(password) * percent)}")

        # - Пароль не должен состоять из повторяющихся букв;
        # Функция вызовется если:
        # кол-во уникального символа будет превышать больше чем 15% от длины всего пароля
        # (округление до ближайшего целого числа)
        # :TODO Нужно лучше настроить весы для часто повторяющегося символа
        if len(password) - len(set(password)) > math.ceil(len(password) * percent):
            """ Объяснение
            Проходим по каждому символу 
            (char - уникальный символ) 
            - Прибавляем символу char_scale += 1
            - С каждым повторением символа: char_scale увеличивается на 1
            - С каждым последующим отличного символа: уменьшаем char_scale на change_scales
            - С каждым уменьшением char_scale, уменьшаем значение decrease_scales
            (Изначально change_scales = 0.61, уменьшаем на 0.11 пока change_scales >= 0.15)
            - Если char_scale превысит 15% от длины пароля => символ встречается слишком много
            """

            # Проверка подряд идущих
            dict_char_scale = {x: 0 for x in set(password)}
            dict_change_scale = {x: change_scales for x in set(password)}
            for letter in password:
                for char, scale in dict_char_scale.items():
                    if letter == char:
                        continue
                    if scale > 0:
                        dict_char_scale[char] -= dict_change_scale[char]
                        if dict_change_scale[char] >= percent:
                            dict_change_scale[char] -= decrease_scales
                        if dict_char_scale[char] < 0:
                            dict_char_scale[char] = 0
                dict_char_scale[letter] += 1
                dict_change_scale[letter] -= decrease_scales
                # print(letter, dict_char_scale)

                if max(dict_char_scale.values()) > len(password) * percent:
                    return "Пароль содержит много повторяющихся букв подряд"

        # Проверка количеств каждого символа на общую длину
        # На каждые 5 символов (1 символ может повторяться 1 раза) (0-4: 1, 5-9: 2, 10-14: 3 ...) 
        for letter in set(password):
            if password.count(letter) > len(password) // 5 + 1:
                return "Пароль содержит много повторяющихся букв"
            
        # Также проверим, что пароль не входит в топ 100_000 популярных паролей 
        if password in list(open("data/password_list_top_100000.txt", 'rb').read()):
            return "Password is too easy"
            
        # print(0, password)
        return "Success"

    return wrapper
