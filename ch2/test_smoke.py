__author__ = 'wangxiao'

import pytest

@pytest.mark.smoke
def test_1():
    assert (1, 2, 3) == (1, 2, 3)

def test_2():
    assert 1 == 2


def test_3():
    assert 2 == 2

@pytest.mark.smoke
def test_4():
    assert 2 != 5