# -*- coding: utf-8 -*-


import random


from telegram.dao.connection import MongoDBConnection


def get_random_quote():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["quotes"].find_one({"_id": str(random.randint(0, generator["quotes"].count()))})
    return result['value']
