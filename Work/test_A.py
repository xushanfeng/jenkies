#!/usr/bin/env python
#encoding:utf-8
import pytest
import allure

class Test_A:

    def setup_class(self):
        pass

    @pytest.allure.testcase('http://my.tms.org/TESTCASE-1')
    @pytest.allure.issue('http://my.tms.org/ISSUE-1')
    @pytest.mark.parametrize("ss, sdfa", [(1, 2), (2, 3)])
    def test_create_channel(self, ss, sdfa):

        allure.attach('描述', '这是一个注册登录的case')
        self.a(ss, sdfa)

    @pytest.mark.parametrize("ss, sdfa", [(1, 2), (2, 3)])
    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_create_channel_1(self, ss, sdfa):
        allure.attach('描述', '这是一个注册登录的case')
        with open("Work/WechatIMG724.PNG", 'r') as f:
            allure.attach("创建测试渠道：%s"%str(ss), f.read(), allure.attach_type.PNG)
        self.a(ss, sdfa)

    @allure.step(title="登录账号:{1},注册:{2}")
    # @allure.step(title="注册:{2}")
    def a(self, black, test):
        return black, test

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_error_case(self):
        allure.attach("描述", "this a error case!")
        print 222
        assert 1 == 2

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_right_case(self):
        allure.attach("描述", "this a right case!")
        assert 1 == 1

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_trivial_case(self):
        allure.attach("trivial", "this is a trivial case!")

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_block_case(self):
        allure.attach("block", "this is a block case!")

    def teardown(self):
        pass
