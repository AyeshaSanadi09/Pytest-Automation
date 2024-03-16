import math

import pytest


@pytest.mark.parametrize("myArray", [55, 33, 77, 99])
def testParam1(myArray):
    assert myArray >= 55


@pytest.mark.parametrize("input,output", [(2, 4), (3, 27), (4, 256)])
def testParam2(input, output):
    assert input ** input == output

data = [
    ([1,2,3],'sum',6),
    ([1,2,3],'prod',6)
]
@pytest.mark.parametrize("a,b,c", data)
def testParam3(a,b,c):
    if b == 'sum':
        assert sum(a) == c
    if b == 'prod':
        assert math.prod(a) == c



