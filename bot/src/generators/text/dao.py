# -*- coding: utf-8 -*-


import random


from src.connection import MongoDBConnection


def get_random_text_prose():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["text_prose"].find_one({
        "_id": str(random.randint(0, generator["text_prose"].count() - 1))
    })
    return result['value']


def get_random_text_business():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["text_business"].find_one({
        "_id": str(random.randint(0, generator["text_business"].count() - 1))
    })
    return result['value']


def get_random_text_science():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["text_science"].find_one({
        "_id": str(random.randint(0, generator["text_science"].count() - 1))
    })
    return result['value']


def get_random_text_humor():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["text_humor"].find_one({
        "_id": str(random.randint(0, generator["text_humor"].count() - 1))
    })
    return result['value']


def get_random_text_home():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["text_home"].find_one({
        "_id": str(random.randint(0, generator["text_home"].count() - 1))
    })
    return result['value']


def get_random_text_med():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["text_med"].find_one({
        "_id": str(random.randint(0, generator["text_med"].count() - 1))
    })
    return result['value']


def get_random_text_lorem():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["text_lorem"].find_one({
        "_id": str(random.randint(0, generator["text_lorem"].count() - 1))
    })
    return result['value']


def get_random_text_fish():
    random.seed()
    generator = MongoDBConnection().get_connection()
    result = generator["text_fish"].find_one({
        "_id": str(random.randint(0, generator["text_fish"].count() - 1))
    })
    return result['value']
