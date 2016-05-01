# -*- coding: utf-8 -*-


from telegram.dao import facts_dao


def generate(params):
    return facts_dao.get_random_quote()
