import pytest

def testRaise():
    with pytest.raises(Exception):
        assert 6/0
        # assert 65>45

def testRaise1():
    with pytest.raises(Exception) as exeInfo:
        assert [1, 2, 3] in [1, 2]
    print(str(exeInfo))

def fun():
    raise ValueError("Exception")

def testRaise2():
    with pytest.raises(Exception) as exeInfo:
        fun()
    assert str(exeInfo) == "Exception"


