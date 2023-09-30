import time
import keyboard

ignored_for_input: set = {'enter', 'backspace', 'caps lock', 'tab',
                          'shift', 'ctr', 'lalt', 'ralt', 'left',
                          'up', 'down', 'right'}


def collect_data_for_input() -> (str, list[float], list[float]):
    chars = []

    intervals = []
    holdings_time = []

    intervals_dict = dict()
    holdings_time_dict = dict()

    def pressed_keys(e):
        if e.event_type == 'down':
            if e.name not in ignored_for_input:
                holdings_time_dict.update({e.name: time.time()})
                if chars and intervals_dict.get(chars[-1], None) is not None:
                    intervals.append(time.time() - intervals_dict[chars[-1]])
                intervals_dict.update({e.name: time.time()})
                chars.append(e.name)
            # if e.name == 'backspace':
            #     chars.pop()
        elif e.event_type == 'up':
            if e.name not in ignored_for_input:
                holdings_time.append(time.time() - holdings_time_dict[e.name])

    keyboard.hook(pressed_keys)
    keyboard.wait('Enter')

    return ''.join(chars), intervals, holdings_time
