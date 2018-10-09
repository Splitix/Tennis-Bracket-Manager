import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'
