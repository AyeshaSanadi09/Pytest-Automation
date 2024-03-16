import pytest

def test_list(setup1):
    setup1.extend(pytest.w2)
    assert setup1 == ["sun","mon","tue","wen","thr","fri","sat"]


def test_factfix(setup4):
    assert type(setup4('list')) == list
    assert type(setup4('tuple')) == tuple

