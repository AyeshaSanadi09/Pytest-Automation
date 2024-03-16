import sys
import pytest

def testStrjoin():
    s1 = 'python,pytest and automation'
    l1 = ['python,pytest','and','automation']
    l2 = ['python','pytest and automation']
    assert ' '.join(l1) == s1


# @pytest.mark.xfail(raises=ValueError) error
@pytest.mark.xfail(raises=IndexError)
def testStr4():
    letters = "abcdefghijklmnopqrstuvwzxy"
    assert letters[33334]

@pytest.mark.xfail(sys.platform=='win32',reason="for practical purpose used")
@pytest.mark.xfail
def testStr5():
    letters = 'abcd'
    num=1234
    assert letters+super == 'abcd1234'