# -*- coding: utf-8 -*-


from pymongo import MongoClient
import os


host = os.environ.get('BOT_MONGODB_HOST')
port = os.environ.get('BOT_MONGODB_PORT')


class MongoDBConnection(object):
    __db = None

    @classmethod
    def get_connection(cls):
        if cls.__db is None:
            cls.__db = MongoClient(host, int(port))['generators']
        return cls.__db
