# -*- coding: utf-8 -*-


from src.generators.jokes import dao


def generate(params):
    return dao.get_random_quote()
