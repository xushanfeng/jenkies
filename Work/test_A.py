#encoding:utf-8
import pytest
import allure

class Test_A:

    def setup_class(self):
        pass

    @pytest.mark.parametrize("ss, sdfa", [(1, 2), (2, 3)])
    def test_create_channel(self, ss, sdfa):
        allure.attach('描述', '这是一个注册登录的case')
        self.a(ss, sdfa)

    @allure.step(title="登录账号:{1},注册:{2}")
    # @allure.step(title="注册:{2}")
    def a(self, balck, test):
        return balck,test

    def teardown(self):
        pass