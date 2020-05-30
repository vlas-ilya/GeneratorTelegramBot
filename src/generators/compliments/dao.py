# -*- coding: utf-8 -*-


import random


from src.connection import MongoDBConnection


def get_random_compliments_for_man_phrase():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["complimentsForMan_phrase"].find_one({
        "_id": str(random.randint(0, generator["complimentsForMan_phrase"].count() - 1))
    })
    return result["value"]


def get_random_compliments_for_man_word():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["complimentsForMan_word"].find_one({
        "_id": str(random.randint(0, generator["complimentsForMan_word"].count() - 1))
    })
    return result["value"]


def get_random_compliments_for_woman_phrase():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["complimentsForWoman_phrase"].find_one({
        "_id": str(random.randint(0, generator["complimentsForWoman_phrase"].count() - 1))
    })
    return result["value"]


def get_random_compliments_for_woman_word():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["complimentsForWoman_word"].find_one({
        "_id": str(random.randint(0, generator["complimentsForWoman_word"].count() - 1))
    })
    return result["value"]



