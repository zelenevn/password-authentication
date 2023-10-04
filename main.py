
from console_controller import Console_controller
from generator import Generator
from overlaps import Overlaps
import matplotlib.pyplot as plt

if __name__ == '__main__':
    alphabet = Console_controller.choose_alphabet()
    length = int(input("L = "))
    print("alphabet:", alphabet)
    generator = Generator(alphabet, length)
    password = generator.get_password()
    print("password: ", password)
    print("start test")

    keys = Overlaps.count_key_overlaps(password)
    plt.title('Задержки между нажатиями, ms')

    plt.plot(
        ['{}-{}'.format(i, i + 1) for i in range(len(keys) - 1)],
        [(keys[i + 1] - keys[i]) * 1000 for i in range(len(keys) - 1)],
        'ro')
    plt.show()


