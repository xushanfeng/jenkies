#encoding:utf-8
import pytest
class Test_A:

    def setup(self):
        pass


    @pytest.mark.parametrize("msg,para",[(u"输入",1111),(u"输出",2222)])
    def test_a(self, msg,para):
        print msg+":",para
        assert 1 == 1
        assert 1 == 2

    def teardown(self):
        pass