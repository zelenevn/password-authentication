import time
import keyboard

ignored_for_input = tuple(['enter', 'backspace', 'caps lock', 'tab', 'shift',
                            'ctr', 'lalt', 'ralt', 'left', 'up', 'down', 'right'])


def data_collection_for_input() -> (str, list[float]):
    chars = []

    pressed_times = []
    intervals = []

    def pressed_keys(e):
        if e.event_type == 'down':
            pressed_times.append(time.time())
        elif e.event_type == 'up':
            if pressed_times:
                intervals.append(time.time() - pressed_times.pop())
            if e.name not in ignored_for_input:
                chars.append(e.name)
            if e.name == 'backspace':
                chars.pop()

    keyboard.hook(pressed_keys)
    keyboard.wait('Enter')

    return ''.join(chars), intervals
