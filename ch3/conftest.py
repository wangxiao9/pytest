__author__ = 'wangxiao'

import pytest
import requests

"""
如果想多个测试用例共享fixture,可以单独建立一个conftest.py 文件，可以看成提供测试用例使用的一个fixture仓库
"""


@pytest.fixture()
def login():
    url = 'http://api.shoumilive.com:83/api/p/login/login/pwd'
    data = {"phone": "18860910", "pwd": "123456"}
    res = requests.post(url, data)
    return res.text

"""
yield: 当执行完对应的testcase后，再回到fixture执行yield中的内容
"""
@pytest.fixture()
def test_yield():
    print("----------------------0")
    yield
    print("----------------------1")


@pytest.fixture()
def one():
    return 1

@pytest.fixture()
def two():
    return 2


@pytest.fixture(name='maoyan')
def test_maoyan_page_001():
    return 2