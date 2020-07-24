__author__ = 'wangxiao'

import pytest

@pytest.mark.smoke
def test_pass():
    assert (1, 2, 3) == (1, 2, 3)


def test_fail():
    assert 1 == 2
