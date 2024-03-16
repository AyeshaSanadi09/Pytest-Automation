import math

import pytest

@pytest.mark.parametrize('list1',[11,22,33,44])
def testParam1(list1):
    assert list1<44

@pytest.mark.parametrize("input,output",[(2,4), (3,27), (4,256)])
def testParam2(input,output):
    assert input**input==output

data=[
    ([2,4,6],'sum',12),
    ([2,4,6],'prod',48)
]
@pytest.mark.parametrize("a,b,c",data)
def testParam3(a,b,c):
    if b=='sum':
        assert c==sum(a)
    elif b=='prod':
        assert c==math.prod(a)