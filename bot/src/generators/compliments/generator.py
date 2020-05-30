# -*- coding: utf-8 -*-


from src.generators.compliments import dao


def generate(params):
    if params.sex == 'man':
        if int(params.type_compl) == 1:
            return dao.get_random_compliments_for_man_word()
        else:
            return dao.get_random_compliments_for_man_phrase()
    else:
        if int(params.type_compl) == 1:
            return dao.get_random_compliments_for_woman_word()
        else:
            return dao.get_random_compliments_for_woman_phrase()
