import pytest

@pytest.fixture()
def getList():
    print("Fixture called....")
    l1=["ayesha","apurva","apeksha"]
    return l1

#simple fixture
def testFixture1(getList):
    print(getList[:])
    assert getList[0]=="ayesha"
    assert getList[-1]=="apeksha"

def revList(list):
    list.reverse()
    return list

#difining fixture as a parameter
def testFixture2(getList):
    assert getList[::-1] == revList(getList)

#calling fixture with marker but that fixture dies not return any value
#So error will generated when we acess getlist fixture=> TypeError: 'function' object is not subscriptable
#to removw or ignore it we use xfail

@pytest.mark.xfail(reason="TypeError: 'function' object is not subscriptable")
@pytest.mark.usefixtures("getList")
def testFixture3():
    assert 1==1
    assert getList[::-1]