# Parameterizing from fixture
import pytest

@pytest.fixture(params=[(1,2),[1,2]], ids=['tuple','list'])
def fixtureParam1(request):
    return request.param

@pytest.fixture(params=['access','slice','assign'])
def fixtureParam2(request):
    return request.param

def testParamFixture1(fixtureParam1):
    assert (type(fixtureParam1)) in [list,tuple]

def testParamFixture2(fixtureParam2,fixtureParam1):
    if(fixtureParam2 == 'access'):
        assert fixtureParam1[0]
    elif(fixtureParam2 == 'slice'):
        assert fixtureParam1[::-1]
    elif(fixtureParam2 == 'assign'):
        assert fixtureParam1[0]