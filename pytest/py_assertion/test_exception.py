import pytest

def testException():
    with pytest.raises(Exception):
        assert 23=="ahh"


def func1():
    raise ValueError("Exception raises....")


def testException1():
    with pytest.raises(Exception) as excinfo:
        # assert 748743>232442223
        func1()
    print(str(excinfo))