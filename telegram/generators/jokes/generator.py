# -*- coding: utf-8 -*-


from telegram.dao import jokes_dao


def generate(params):
    return jokes_dao.get_random_quote()
