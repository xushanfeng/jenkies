#encoding:utf-8
import pytest
class Test_A:

    def setup(self):
        pass


    @pytest.mark.parametrize("msg,para",[("输入",1111),("输出",2222)])
    def test_a(self, msg,para):
        print str(msg).encode("gbk")+":",para
        assert 1 == 1

    def teardown(self):
        pass