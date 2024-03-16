import pytest
import sys

# to skip whole module based on condition
# pytestmark=pytest.mark.skipif(sys.platform=='win32',reason="use linux system")

const=9/5
def cal_to_far(cal=0):
    far=(const*cal)+32
    return far

# print(cal_to_far())
# to skip test function
@pytest.mark.skip(reason="for my use skipped")
def testA1():
    assert type(cal_to_far())==float

# to skip test function based on condition
@pytest.mark.skipif(pytest.__version__!=7.3,reason="install pytest")
def testA2():
    assert cal_to_far()==32

#skip using custom function
@pytest.mark.skipif(cal_to_far()==32,reason="default value given")
def testA3():
    assert cal_to_far(140)==284

