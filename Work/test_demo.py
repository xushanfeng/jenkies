#!/usr/bin/env python
#encoding:utf-8
'''
此实例仅作allure示范使用
'''

import pytest
import allure
from demo import sum

class Test_Demo:

    def setup(self):
        pass

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_level(self):
        '''
        增加测试级别
        TRIVIAL:低
        MINOR:普通
        NORMAL:普通
        CRITICAL:严重
        BLOCKER:崩溃
        :return:
        '''
        allure.attach("新增级别", "这是一个新增的测试级别")

    def test_add_attach(self):
        '''
        增加附件到用例
        支持类型：
        HTML
        JPG
        PNG
        JSON
        OTHER
        TEXTXML
        '''
        allure.attach("新增附件", "这是一个新增的测试附件")
        with open("Work/WechatIMG724.JPG", 'r') as f:
            allure.attach("吃惊", f.read(), allure.attach_type.JPG )
        with open("Work/TYPE.JSON", 'r') as f:
            allure.attach("Json String", f.read(), allure.attach_type.JSON )

    @pytest.allure.issue("http://www.baidu.com")
    def test_add_issue(self):
        '''
        将问题与当前case关联
        :return:
        '''
        allure.attach("关联问题","通过装饰器将问题与用例关联")

    def test_add_testcase(self):
        '''
        新增测试用例
        :return:
        '''
        allure.attach("新增用例", "这是一个新增的测试用例")


    def test_add_discr(self):
        '''
        这仅仅是一个描述
        :return:
        '''
        allure.attach("新增描述", "这是一个新增的用例描述")

    @allure.feature("登录")
    @allure.story('管理员')
    def test_add_first_feature_a(self):
        '''
        这仅仅是一个描述
        :return:
        '''
        allure.attach("新增功能模块", "这是一个新增的功能模块")


    @allure.feature("登录")
    @allure.story('业务员')
    def test_add_first_feature_b(self):
        '''
        这仅仅是一个描述
        :return:
        '''
        allure.attach("新增功能模块", "这是一个新增的功能模块")

    @allure.feature("注册")
    @allure.story('忘记密码')
    def test_add_second_feature_a(self):
        '''
        这仅仅是一个描述
        :return:
        '''
        allure.attach("新增功能模块", "这是一个新增的功能模块")


    @allure.feature("注册")
    @allure.story('找回密码')
    def test_add_second_feature_b(self):
        '''
        这仅仅是一个描述
        :return:
        '''
        allure.attach("新增功能模块", "这是一个新增的功能模块")