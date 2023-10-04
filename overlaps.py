import time

import keyboard


class Overlaps:
    @staticmethod
    def count_key_overlaps(password):
        count = 0
        times = []
        while count <= len(password):
            K = keyboard.read_key()
            if keyboard.is_pressed(K):
                count += 1
                times.append(time.time())
        return times