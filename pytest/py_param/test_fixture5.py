 # parameerization with fixture
import pytest

@pytest.fixture(params=[(1,2,3),[1,2,3]],ids=["tuple","list"])
def test_setupFixture1(request):
     return request.param

@pytest.fixture(params= ["assign",'access',"slice","len"])
def test_setupFixture2(request):
     return request.param


def test_request1(test_setupFixture1):
     assert type(test_setupFixture1) in [list, tuple]

def test_request2(test_setupFixture1,test_setupFixture2):
     if test_setupFixture2 == 'assign':
         test_setupFixture1[0] = 99
         assert True
     elif test_setupFixture2 == 'len':
         assert len(test_setupFixture1)
     elif test_setupFixture2 == 'access':
         assert test_setupFixture1[0]
     else:
         assert test_setupFixture1[::-1]