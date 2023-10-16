
import numpy as np
from PIL import Image, ImageChops

from scipy.fftpack import dct, idct


def tobits(s):
    result = []  # создание пустого списка для хранения битов
    for c in s:  # проходим по символам строки s
        bits = bin(ord(c))[2:]  # получаем двоичное представление символа
        bits = '00000000'[len(bits):] + bits  # дополняем нулями до 8 бит
        result.extend([int(b) for b in bits])  # добавляем каждый бит в список result
    return result  # возвращаем список битов


def frombits(bits):
    chars = []  # создание пустого списка для хранения символов
    for b in range(len(bits) // 8):  # проходим по каждому байту в списке битов
        byte = bits[b*8:(b+1)*8]  # извлекаем 8 бит, соответствующих текущему байту
        # преобразуем 8 бит в символ и добавляем его в список chars
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)  # объединяем все символы в строку и возвращаем ее


def round_pixel_value(pixel_value):
    pixel_value = round(pixel_value)  # округляем значение пикселя
    if pixel_value > 255:  # если значение больше 255, то ограничиваем его до 255
        pixel_value = 255
    elif pixel_value < 0:  # если значение меньше 0, то ограничиваем его до 0
        pixel_value = 0
    return pixel_value  # возвращаем ограниченное значение


def block_dct(image: Image, block_size, block_row, block_column, channel: int):
    channel_values = []  # создание пустого списка для хранения значений канала
    for x in range(block_size * block_row, block_size * block_row + block_size):  # проходим по координатам x в блоке
        # проходим по координатам y в блоке
        for y in range(block_size * block_column, block_size * block_column + block_size):
            # получаем значение канала для текущего пикселя и добавляем его в список
            channel_values.append(image.getpixel((x, y))[channel])
    # вычисляем дискретное косинусное преобразование (DCT) для списка значений канала и возвращаем его
    return dct(channel_values)


def image_idct(dct, image: Image, block_size, block_row, block_column, channel: int):
    # применяем обратное дискретное косинусное преобразование (IDCT) к переданному списку коэффициентов DCT
    channel_values = idct(dct)
    i = 0  # инициализируем переменную i, которая будет использоваться для индексирования списка channel_values
    width, height = image.size  # получаем размеры изображения
    for x in range(block_size * block_row, block_size * block_row + block_size):  # проходим по координатам x в блоке
        # проходим по координатам y в блоке
        for y in range(block_size * block_column, block_size * block_column + block_size):
            pixel = list(image.getpixel((x, y)))  # получаем значения пикселя в виде списка [R, G, B]
            # заменяем значение канала на соответствующее значение из списка channel_values и округляем его
            pixel[channel] = round_pixel_value(channel_values[i])
            image.putpixel((x, y), tuple(pixel))  # заменяем пиксель на новое значение
            i += 1  # увеличиваем индекс для списка channel_values
    return image  # возвращаем измененное изображение


def get_new_dct_value(dct_value, bit, power):
    # Функция принимает значение коэффициента DCT, бит и степень сжатия
    # Если бит равен 1, то значение бита равно 1, иначе -1
    # Вычисляем новое значение коэффициента DCT с учетом бита и степени сжатия
    return dct_value * (1 + power * (bit if bit == 1 else -1))


def cox_encode(image: Image, message_bits, power=2, block_size=8):
    # Функция принимает изображение, биты сообщения, степень сжатия и размер блока
    # Создаем копию изображения
    image_with_message = image.copy()
    # Получаем размеры изображения
    width, height = image.size
    # Вычисляем количество блоков по строкам и столбцам
    blocks_row_count = height // block_size
    blocks_column_count = width // block_size
    # Проходимся по каждому биту сообщения и изменяем соответствующий коэффициент DCT
    for index, bit in enumerate(message_bits):
        # Вычисляем номер строки и столбца блока
        block_row_index = index % blocks_row_count
        block_column_index = index // blocks_row_count
        # Получаем значения коэффициентов DCT для блока
        dct_values = block_dct(image, block_size, block_row_index, block_column_index, 2)
        # Находим индекс максимального значения коэффициента DCT и изменяем его значение
        max_index = dct_values.argmax()
        dct_values[max_index] = get_new_dct_value(dct_values[max_index], bit, power)
        # Применяем обратное преобразование DCT и изменяем соответствующие пиксели в копии изображения
        image_idct(dct_values, image_with_message, block_size, block_row_index, block_column_index, 2)
    # Возвращаем изображение с сообщением
    return image_with_message


def cox_decode(image_original: Image, image_distorted: Image, message_bits_length, block_size=8):
    # Инициализируем пустой список для хранения бит сообщения
    message_bits = []
    width, height = image_original.size
    # Вычисляем количество блоков по строкам и столбцам
    blocks_row_count = height // block_size
    blocks_column_count = width // block_size
    # Проходим по каждому биту сообщения
    for index in range(message_bits_length):
        # Вычисляем индекс строки блока
        block_row_index = index % blocks_row_count
        # Вычисляем индекс столбца блока
        block_column_index = index // blocks_row_count
        # Вычисляем DCT коэффициенты для соответствующего блока на оригинальном и искаженном изображении
        dct_values1 = block_dct(image_original, block_size, block_row_index, block_column_index, 2)
        dct_values2 = block_dct(image_distorted, block_size, block_row_index, block_column_index, 2)
        # Находим индекс максимального коэффициента DCT в блоке
        max_index = dct_values1.argmax()
        # Получаем значения DCT коэффициентов для оригинального и искаженного изображений
        dct_value1 = dct_values1[max_index]
        dct_value2 = dct_values2[max_index]
        # Сравниваем значения коэффициентов и добавляем соответствующий бит в сообщение
        if dct_value2 > dct_value1:
            message_bits.append(1)
        else:
            message_bits.append(0)
    # Возвращаем список бит сообщения
    return message_bits


# Определяемы строку, которую будем скрывать в изображении
data = 'Hello There Steg'
# Преобразуем строку в последовательность битов
data_bits = tobits(data)

# Открываем оригинальное изображение, в которое будем скрывать сообщение
img_original = Image.open('in.png')

# Кодируем сообщение в изображение
img_with_message = cox_encode(img_original, data_bits)
# Сохраняем полученное изображение с сообщением в файл
img_with_message.save('out.png')

# Декодируем сообщение из изображения
message = cox_decode(img_original, img_with_message, len(data_bits))
# Преобразуем последовательность битов обратно в строку
decoded_data = frombits(message)

# Выводим декодированное сообщение в консоль
print(decoded_data)

# Открываем полученное изображение с сообщением
img_encode = Image.open('out.png')


def maxd(img1, img2):
    # Загружаем пиксели изображений в переменные pixels1 и pixels2
    pixels1 = img1.load()
    pixels2 = img2.load()
    # Устанавливаем начальное значение переменной diff в 0
    diff = 0
    # Проходим по всем пикселям изображения
    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            if pixels1[i, j] != pixels2[i, j]:
                diff = 1
    # Возвращаем значение переменной diff
    return diff


def nc(image1: Image, image2: Image, channel: int):
    # Функция вычисляет нормализованный кросс-корреляционный коэффициент (NC) для заданных канала и двух изображений
    # Получаем размеры изображений
    width, height = image1.size
    # Обнуляем переменные для хранения суммы произведений и квадратов значений пикселей
    image_diff_sum = 0
    image_square_sum = 0
    # Обходим все пиксели обоих изображений
    for x in range(0, width):
        for y in range(0, height):
            # Получаем значения пикселей для обоих изображений
            image1_pixel_value = image1.getpixel((x, y))[channel]
            image2_pixel_value = image2.getpixel((x, y))[channel]
            # Вычисляем сумму произведений значений пикселей
            image_diff_sum += image1_pixel_value * image2_pixel_value
            # Вычисляем сумму квадратов значений пикселей первого изображения
            image_square_sum += image1_pixel_value * image1_pixel_value
    # Вычисляем нормализованный кросс-корреляционный коэффициент
    return image_diff_sum / image_square_sum


def uqi(img1: Image, img2: Image):
    # Получаем значения пикселей в виде массивов
    img1 = np.array(img1, dtype=np.float32)
    img2 = np.array(img2, dtype=np.float32)

    # Вычисляем ковариационную матрицу
    cov_matrix = np.cov(np.ravel(img1), np.ravel(img2))
    cov = cov_matrix[0, 1]

    # Вычисляем дисперсии каждой картинки
    img1_var = np.var(img1)
    img2_var = np.var(img2)

    # Вычисляем коэффициент UQI
    numerator = (2 * cov + 0.01)
    denominator = (img1_var + img2_var + 0.01)
    uqi = numerator / denominator

    return uqi


print('maxd = ', maxd(img_original, img_encode))
print(f'nc = {nc(img_original, img_with_message, 2)}')
print(f'uqi = {uqi(img_original, img_with_message)}')