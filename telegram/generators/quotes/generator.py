# -*- coding: utf-8 -*-


from telegram.dao import quotes_dao


def generate(params):
    return quotes_dao.get_random_quote()
