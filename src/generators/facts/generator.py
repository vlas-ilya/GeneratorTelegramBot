# -*- coding: utf-8 -*-


from src.generators.facts import dao


def generate(params):
    return dao.get_random_quote()
