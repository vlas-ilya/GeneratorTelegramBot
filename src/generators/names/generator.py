# -*- coding: utf-8 -*-


import random

from src.generators.names import dao
from src.generators.names.nicknames import generator as nicknames


def _generate_man_name(_surname, _name, _patronymic):
    name = []
    if _surname == 1:
        name.append(dao.get_random_man_f())
    if _name == 1:
        name.append(dao.get_random_man_i())
    if _patronymic == 1:
        name.append(dao.get_random_man_o())
    return " ".join(name)


def _generate_woman_name(_surname, _name, _patronymic):
    name = []
    if _surname == 1:
        name.append(dao.get_random_woman_f())
    if _name == 1:
        name.append(dao.get_random_woman_i())
    if _patronymic == 1:
        name.append(dao.get_random_woman_o())
    return " ".join(name)


def _generate(sex, _surname, _name, _patronymic):
    if sex == "all":
        sex = "man" if random.randint(0, 1) == 1 else "woman"
    if sex == "man":
        return _generate_man_name(int(_surname), int(_name), int(_patronymic))
    elif sex == "woman":
        return _generate_woman_name(int(_surname), int(_name), int(_patronymic))


def generate(params):
    count = min(100, int(params.count))
    _surname = params.surname
    _name = params.name
    _patronymic = params.patronymic
    sex = params.sex
    if sex == 'nick':
        return "\n".join(nicknames.generate(int(count)))
    else:
        random.seed()
        return "\n".join([_generate(sex, _surname, _name, _patronymic) for _ in range(0, int(count))])
