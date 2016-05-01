# -*- coding: utf-8 -*-


import random


from telegram.dao.connection import MongoDBConnection


def get_random_man_f():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["nameForMan_f"].find_one({
        "_id": str(random.randint(0, generator["nameForMan_f"].count() - 1))
    })
    return result['value']


def get_random_man_i():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["nameForMan_i"].find_one({
        "_id": str(random.randint(0, generator["nameForMan_i"].count() - 1))
    })
    return result['value']


def get_random_man_o():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["nameForMan_o"].find_one({
        "_id": str(random.randint(0, generator["nameForMan_o"].count() - 1))
    })
    return result['value']


def get_random_woman_f():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["nameForWoman_f"].find_one({
        "_id": str(random.randint(0, generator["nameForWoman_f"].count() - 1))
    })
    return result['value']


def get_random_woman_i():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["nameForWoman_i"].find_one({
        "_id": str(random.randint(0, generator["nameForWoman_i"].count() - 1))
    })
    return result['value']


def get_random_woman_o():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["nameForWoman_o"].find_one({
        "_id": str(random.randint(0, generator["nameForWoman_o"].count() - 1))
    })
    return result['value']
