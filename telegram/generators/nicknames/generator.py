# -*- coding: utf-8 -*-


import random
import math


from telegram.generators.nicknames.prefixes import prefix
from telegram.generators.nicknames.suffixes import suffix


def _generate():
    random.seed()
    count_types = min(len(prefix), len(suffix))
    type_index = math.floor(random.random() * count_types)
    prefix_variants, suffix_variants = prefix[type_index], suffix[type_index]
    prefix_index = math.floor(random.random() * len(prefix_variants))
    suffix_index = math.floor(random.random() * len(suffix_variants))
    return prefix_variants[prefix_index] + suffix_variants[suffix_index]


def generate(count):
    count = 100 if count > 100 else count
    return [_generate() for _ in range(0, count)]
