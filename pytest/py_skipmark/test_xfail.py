import sys
import pytest

def testStrJoin():
    str4 = ['python,pytest','and','automation']
    assert ' '.join(str4) == "python,pytest and automation"

@pytest.mark.xfail(sys.platform == 'linux',reason = 'used for demo purpose')
def testStrLen5():
    str5 = 'hii ayesha'
    assert len(str5) == 24

@pytest.mark.xfail(raises = IndexError, reason='index error')
def testStr():
    str5 = 'hii ayesha'
    assert str5[134]

@pytest.mark.xfail
def testStr6():
    str6 = "hii"
    str62 = 'ayesha'
    assert str6+str62 == 'hii ayesha'