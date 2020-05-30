# -*- coding: utf-8 -*-


import random


def _generate(length, symbols):
    return "".join([symbols[random.randint(0, len(symbols) - 1)] for _ in range(0, length)])


def _symbols(num, lower, upper, symbols):
    result = ''
    if num == '1':
        result += '0123456789' * 2
    if lower == '1':
        result += 'abcdefjhijklmnopqrstuvwxyz' * 2
    if upper == '1':
        result += 'ABCDEFJHIJKLMNOPQRSTUVWXYZ' * 2
    if symbols == '1':
        result += '!#-$%_^&*_()_[]-~.,|+_-='
    return result if len(result) > 0 else '0123456789abcdefjhijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ'


def generate(params):
    random.seed()
    symbols = _symbols(params.num, params.lower, params.upper, params.symbol)
    return '\n'.join(_generate(min(36, int(params.count)), symbols) for _ in range(0, 10))
