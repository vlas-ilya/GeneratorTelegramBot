# -*- coding: utf-8 -*-


from telegram.dao import compliments_dao


def generate(params):
    if params.sex == 'man':
        if int(params.type_compl) == 1:
            return compliments_dao.get_random_compliments_for_man_word()
        else:
            return compliments_dao.get_random_compliments_for_man_phrase()
    else:
        if int(params.type_compl) == 1:
            return compliments_dao.get_random_compliments_for_woman_word()
        else:
            return compliments_dao.get_random_compliments_for_woman_phrase()
