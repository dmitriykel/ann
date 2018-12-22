import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or 'upload/'
