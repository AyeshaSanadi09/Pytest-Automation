import pytest

@pytest.fixture
def setupList():
    print("\nInside the Fixture..")
    name = ["Ayesha","Apurva","Apeksha","Fija","Pratiksha"]
    return name

def test_fixture1(setupList):
    print(setupList[:])
    assert setupList[0] == 'Ayesha'
    assert setupList[2:4] == ['Apeksha','Fija']

def reverseList(list):
    list.reverse()
    return list

def test_fixture2(setupList):
    assert setupList[::-2] ==  ["Pratiksha",'Apeksha',"Ayesha"]
    assert setupList[::-1] == reverseList(setupList)

@pytest.mark.xfail(reason="TypeError: 'function' object is not subscriptable")
@pytest.mark.usefixtures("setupList")
def test_fixture3():
    assert setupList[0]
