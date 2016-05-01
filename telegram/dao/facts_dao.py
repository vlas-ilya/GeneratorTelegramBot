# -*- coding: utf-8 -*-


import random


from telegram.dao.connection import MongoDBConnection


def get_random_quote():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["facts"].find_one({"_id": str(random.randint(0, generator["facts"].count() - 1))})
    return result['value']
