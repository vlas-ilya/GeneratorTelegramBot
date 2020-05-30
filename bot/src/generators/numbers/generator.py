# -*- coding: utf-8 -*-


import random


def _random(miv_value, max_value):
    random.seed()
    return random.randint(miv_value, max_value)


def _get_separator(separator):
    if separator == 'space':
        return ' '
    elif separator == 'comma':
        return ','
    elif separator == 'spacecomma':
        return ', '
    else:
        return separator


def _try_get_unique_random(min_value, max_value, randoms):
    for i in range(0, 5):
        number = _random(min_value, max_value)
        if number not in randoms:
            randoms.append(number)
            return


def _generate(min_value, max_value, count, separator, repeat):
    if repeat == "0":
        return _get_separator(separator).join([str(_random(min_value, max_value)) for _ in range(0, count)])
    else:
        result = []
        for i in range(0, count):
            _try_get_unique_random(min_value, max_value, result)
        return _get_separator(separator).join([str(x) for x in result])


def generate(params):
    min_value = params.min
    max_value = params.max
    count = min(100, int(params.count))
    separator = params.separator
    repeat = params.repeat
    return _generate(int(min_value), int(max_value), int(count), separator, repeat)
