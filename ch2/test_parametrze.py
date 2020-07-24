__author__ = 'wangxiao'

import pytest

"""
参数化
"""


def add(a, b):
    return a + b


# 根据对应参数赋值
@pytest.mark.parametrize('a,b', [(1, 2), (2, 4)])
def test_add_01(a, b):
    sum = add(a, b)
    assert sum == 3


# 根据对象赋值
@pytest.mark.parametrize('add', [add(1, 2), add(2, 4)])
def test_add_02(add):
    sum = add
    assert sum == 3


# 通过自定义id作为标识
@pytest.mark.parametrize('add', [pytest.param(add(1, 2), id='success'), pytest.param(add(2, 4), id='fail')])
def test_add_03(add):
    sum = add
    assert sum == 3