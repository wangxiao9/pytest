__author__ = 'wangxiao'

import pytest

"""
fixture :
    @pytest.fixture
    声明了一个fixture,如果测试函数中用到fixture名，那么pytest会检测到，并且再执行测试用例前，先执行fixture
"""

@pytest.fixture()
def data():
    return 3

def test_data(data):
    assert data == 4