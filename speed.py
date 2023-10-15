from datetime import datetime


def speed_array(start_times):
    intervals = list()
    n = len(start_times)
    for i in range(1, n):
        intervals.append((start_times[i].second - start_times[i - 1].second) + (
                    start_times[i].microsecond - start_times[i - 1].microsecond) / 10e6)
    return intervals


def update_time():
    return datetime.now()
