#encoding:utf-8
'''
应用程序需要一些配置，比如对于开发、测试、产品会需要不同的数据库那样才不会相互影响。
和单文件版本中在hello.py中写所有的配置不同，我们能够用类层级的方式来组织配置

为了让配置更灵活、安全，一些配置参数可以从环境变量中导入，
比如SECRET_KEY考虑到安全性，可以存储在环境变量中，并且在配置脚本中提供了一个默认值以防环境变量没有设置它。
'''
import os
basedir = os.path.abspath(os.path.dirname(__file__))
# print (basedir)
# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
#     SQLALCHEMY_COMMIT_ON_TEARDOWN = True
#     SQLALCHEMY_TRACK_MODIFICATIONS = True
#     FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
#     FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
#     FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
#
#     @staticmethod
#     def init_app(app):
#         pass


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = '2681590688@qq.com'
    FLASKY_ADMIN = '904159574@qq.com'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}