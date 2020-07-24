__author__ = 'wangxiao'

import pytest
from selenium import webdriver


@pytest.fixture(name='loginMaoYan')
def open_maoyan():
    executable_path = 'C://Users//z0040utb//driver//chromedriver_win32//chromedriver.exe'
    driver = webdriver.Chrome(executable_path=executable_path)
    return driver
