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
    def test_create_channel_1(self, ss, sdfa):
        allure.attach('描述', '这是一个注册登录的case')
        f = open("Work/WechatIMG724.PNG",'r').read()
        allure.attach("创建测试渠道：%s"%str(ss),f, allure.attach_type.PNG)
        self.a(ss, sdfa)

    @allure.step(title="登录账号:{1},注册:{2}")
    # @allure.step(title="注册:{2}")
    def a(self, balck, test):
        return balck,test

    def teardown(self):
        pass