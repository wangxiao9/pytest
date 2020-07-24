__author__ = 'wangxiao'

from time import sleep

import pytest


def test_page(loginMaoYan):
    driver = loginMaoYan
    driver.get("https://maoyan.com/")
    sleep(2)