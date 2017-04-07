#encoding:utf-8

'''
在单文件版本中创建应用程序实例很方便，但是通常会有缺陷。因为应用程序实例在全局作用于下被创建，而实例被创建后是没办法动态修改配置的。
尤其在做单元测试时，因为要跑不同的数据库，所以我们要应用不同的配置。

解决办法就是通过使用工厂方法延迟应用程序实例的创建，这样不仅仅是延迟了创建时间还让脚本有创建多个应用程序实例的能力，这对于测试尤其有用。
Example 7-3中在app包中定义了了这样一个工厂方法。

app包导入了Flask目前会用到的扩展，但因为应用程序实例还没有被构建出来，它们都还没有被正确初始化。
create_app()这个工厂方法接受一个配置名称作为参数，通过使用Flask提供的app.config的from_object()方法，
我们就能从config.py中导入所需要的配置。一旦应用程序实例被创建出来，扩展就能够通过调用init_app()来完成初始化。
'''

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    # attach routes and custom error pages here
    # from main \
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
