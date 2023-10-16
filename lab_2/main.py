from PIL import Image
import numpy as np


def char_to_bin(char):
    return bin(ord(char))[2:].zfill(8)


def string_to_bin(string):
    return ''.join([char_to_bin(char) for char in string])


def cjbc(message, cover_path, stego_path):
    # Загрузка изображения-носителя
    cover = Image.open(cover_path)

    # Проверка размеров изображения
    if cover.size[0] * cover.size[1] * 8 < 24 + 8 * len(message + '\x00'):
        print("Cover image too small to embed data!")
        return

    # Конвертация в массив NumPy
    cover = np.array(cover)

    # Добавление признака встраивания
    embed_string_bin = string_to_bin(message + '\x00')
    embed_string_bin_len = len(embed_string_bin)
    if embed_string_bin_len % 8 != 0:
        embed_string_bin += '0' * (8 - embed_string_bin_len % 8)
    embed_string_bin += '11111111'

    # Индексация пикселей и RGBA-каналов
    rows, cols, rgb = cover.shape
    b = cover[:, :, 2].flatten().tolist()
    b_idx = 0

    for bit in embed_string_bin:
        # Получение компонент
        x, y = b_idx // cols, b_idx % cols
        lsb = b[b_idx] & 1

        # Встраивание бита
        if lsb != int(bit):
            b[b_idx] = (b[b_idx] & ~1) | int(bit)

        b_idx += 1

    # Конвертация обратно в изображение
    b = np.array(b).reshape((rows, cols))
    stego = Image.fromarray(np.dstack([cover[:, :, 0], cover[:, :, 1], b]).astype('uint8'))
    stego.save(stego_path)


def cjbc_extract(stego_path):
    # Загрузка изображения-носителя
    stego = Image.open(stego_path)

    # Конвертация в массив NumPy
    stego = np.array(stego)

    # Индексация пикселей и RGBA-каналов
    rows, cols, rgb = stego.shape
    b = stego[:, :, 2].flatten().tolist()
    b_idx = 0

    # Поиск признака встраивания
    embed_bits = []
    current_bits = []
    while current_bits != [1, 1, 1, 1, 1, 1, 1, 1]:
        if b_idx >= len(b):  # проверяем, не закончился ли список b
            break
        x, y = b_idx // cols, b_idx % cols
        lsb = b[b_idx] & 1
        current_bits.append(lsb)
        b_idx += 1
        if len(current_bits) == 8:
            embed_bits.extend(current_bits)
            current_bits = []

    # Получение скрытой строки
    embed_string = ''
    for i in range(0, len(embed_bits), 8):
        byte = ''.join([str(bit) for bit in embed_bits[i:i + 8]])
        char = chr(int(byte, 2))
        embed_string += char
        if char == '\x00':
            break

    return embed_string[:-1]


data = 'Very secret information'
# Встраивание строки в изображение
cjbc(data, 'image.jpg', 'stego.png')

# Извлечение
print(cjbc_extract('stego.png'))


def max_abs_error(y_true, y_pred):
    max_d = np.max(np.abs(y_true.astype(int) - y_pred.astype(int)))
    return max_d


def nrmse(y_true, y_pred):
    num = np.sqrt(np.mean(np.square(y_true - y_pred)))
    denom = np.max(y_true) - np.min(y_true)
    return num / denom


def uiq(y_true, y_pred):
    num = np.mean(y_true * y_pred)
    denom = np.sqrt(np.mean(np.square(y_true))) * np.sqrt(np.mean(np.square(y_pred)))
    return num / denom


def metrics(orig, steg):
    image = Image.open(orig)
    image2 = Image.open(steg)
    image_arr = np.array(image)
    image2_arr = np.array(image2)
    print("Максимальное абсолютное отклонение: ", max_abs_error(image_arr, image2_arr))
    print("Нормированное среднее квадратичное отклонение: ", nrmse(image_arr, image2_arr))
    print("Универсальный индекс качества: ", uiq(image_arr, image2_arr))


metrics('image.jpg', 'stego.png')
