# -*- coding: utf-8 -*-


import copy


import telegram.generators.text.generator as text
import telegram.generators.quotes.generator as quotes
import telegram.generators.passwords.generator as passwords
import telegram.generators.numbers.generator as numbers
import telegram.generators.compliments.generator as compliments
import telegram.generators.facts.generator as facts
import telegram.generators.inn.generator as inn
import telegram.generators.jokes.generator as jokes
import telegram.generators.names.generator as names
import telegram.generators.nicknames.generator as nicknames


class Parameters:
    def __init__(self):
        self.paragraph = 1
        self.word = 60
        self.type = 'fish'
        self.min = 1
        self.max = 100
        self.count = 10
        self.separator = 'spacecomma'
        self.repeat = 1
        self.surname = 1
        self.name = 1
        self.patronymic = 1
        self.sex = 'all'
        self.type_compl = 0
        self.num = 1
        self.lower = 1
        self.upper = 1
        self.symbol = 1
        self.inn = ""


generators = {
    "text": lambda params: text.generate(params),
    "quotes": lambda params: quotes.generate(params),
    "passwords": lambda params: passwords.generate(params),
    "numbers": lambda params: numbers.generate(params),
    "compliments": lambda params: compliments.generate(params),
    "facts": lambda params: facts.generate(params),
    "inn": lambda params: inn.generate(params),
    "jokes": lambda params: jokes.generate(params),
    "names": lambda params: names.generate(params),
    "nicknames": lambda params: nicknames.generate(params)
}


def transform(params):
    params = copy.deepcopy(params)
    processor = params.pop('processor')
    processor += ' '
    for key in params.keys():
        processor += key + "=" + params[key] + " "
    return processor[:-1]


def get_field(field_name, params, default_value):
    return params.get(field_name) if params.get(field_name) is not None else default_value


def generate(params):
    processor = params['processor']
    generator = generators[processor]

    if generator is None:
        return "Не удалось распознать тип генератора, попробуйте еще раз"

    params = dict(map(lambda l: (l[0], l[1]), map(lambda elem: elem.split('='), transform(params).split(' ')[1:])))
    p = Parameters()

    p.paragraph = get_field('paragraph', params, p.paragraph)
    p.word = get_field('word', params, p.word)
    p.type = get_field('type', params, p.type)
    p.min = get_field('min', params, p.min)
    p.max = get_field('max', params, p.max)
    p.count = get_field('count', params, p.count)
    p.separator = get_field('separator', params, p.separator)
    p.repeat = get_field('repeat', params, p.repeat)
    p.surname = get_field('surname', params, p.surname)
    p.name = get_field('name', params, p.name)
    p.patronymic = get_field('patronymic', params, p.patronymic)
    p.num = get_field('num', params, p.num)
    p.lower = get_field('lower', params, p.lower)
    p.upper = get_field('upper', params, p.upper)
    p.symbol = get_field('symbol', params, p.symbol)
    p.sex = get_field('sex', params, p.sex)
    p.type_compl = get_field('type_compl', params, p.type_compl)
    p.inn = get_field('inn', params, p.inn)
    p.type = get_field('type', params, p.type)

    return generator(p)
