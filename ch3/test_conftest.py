__author__ = 'wangxiao'

import json

import pytest

"""
通过conftest 建立公共仓库，testcase获取公共仓库
"""
@pytest.mark.login
def test_conftest(login):
    data = json.loads(login)
    print(data['code'])
    assert data['code'] == '200'

"""
使用yield
"""
@pytest.mark.y
@pytest.mark.usefixtures('test_yield')
def test_yield():
    print("------------test-----------")


if __name__ == '__main__':
    pytest.main(["--setup-show", "-m", "login", "-s", "-v"])
