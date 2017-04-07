#encoding: utf-8

'''
测试是按照Python包中的典型的单元测试的写法来构建的，setUp() 和 tearDown() 方法在每个测试方法执行前后都会运行，
任何以test_ 开头的方法都会被当做测试方法来执行。关于使用Python包来做单元测试的更多信息可以查看official documentation。

setUp()方法创建了测试所需的环境， 他首先创建了应用程序实例用作测试的山下文环境，这样就能确保测试拿到current_app,
然后新建了一个全新的数据库。数据库和应用程序实例最后都会在tearDown() 方法被销毁。

第一个测试确保了应用程序实例是存在的，第二个测试应用程序实例在测试配置下运行。
为了确保测试文件夹有正确的包结构，我们需要添加一个tests/__init__.py文件（注：涉及Python包相关知识），
这样单元测试包就能扫描所有在测试文件夹中的模块了。

'''
import unittest
from flask import current_app
from app import create_app, db


class BasicsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

