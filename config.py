# -*- coding: utf-8 -*-
import os
import pymysql

SECRET_KEY = 'cdd1588cfcc64ef1ac7b253daf34a973'
FLASKY_ADMIN = '111111@qq.com'
MAIL_USERNAME = '222222@qq.com'
MAIL_PASSWORD = 'XXXXXX'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/blog'
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SECRET_KEY = SECRET_KEY or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASK_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flask Admin<flasky@example.com'
    # FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASKY_ADMIN = FLASKY_ADMIN

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_USERNAME = MAIL_USERNAME
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_PASSWORD = MAIL_PASSWORD
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or 'sqllite:///' + os.path.join(basedir,
    #                                                                                              'data.dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or 'sqllite:///' + os.path.join(basedir,
    #                                                                                              'data.dev.sqlite')
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
