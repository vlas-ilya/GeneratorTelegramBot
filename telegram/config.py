# -*- coding: utf-8 -*-


import os

token = os.environ.get('PRODUCTION_TOKEN')
token = os.environ.get('TEST_TOKEN') if token is None else token
