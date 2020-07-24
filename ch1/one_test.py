__author__ = 'wangxiao'

import pytest


def test_1():
    assert (1, 2, 3) == (1, 2, 3)

@pytest.mark.smoke
def test_2():
    assert 1 == 2
