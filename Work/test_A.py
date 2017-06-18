import pytest
class Test_A:

    def setup(self):
        pass


    @pytest.mark.parametrize("a",[(111),(2222)])
    def test_a(self, a):
        print a
        assert 1 == 1

    def teardown(self):
        pass