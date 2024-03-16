import pytest

#declaring namespace
# syntax def pytestNameSpaceName
def pytest_configure():
    pytest.weekdays1 = ["sun","mon","tues"]
    pytest.weekdays2 = ["thrs","fri","sat"]

@pytest.fixture(scope='module')
def setup1():
    print("setup method called...")
    w1=pytest.weekdays1.copy()
    w1.append("wen")
    yield w1
    print("value is return from setup1 method")
    w1.pop()

@pytest.fixture()
def setup2():
    print("setup2 method called...")
    w2=pytest.weekdays2.copy()
    w2.insert(0,"wen")
    yield w2
    print("value is return from setup2 method")
    w2.pop()

#using request
@pytest.fixture()
def setup3(request):
    m = getattr(request.module,"months")
    print("Scope is: "+str(request.scope))
    print("Function name is: "+str(request.function.__name__))
    print("Module/File name is: "+str(request.module.__name__))
    m.append('April')
    m.append('May')
    yield m
    print(m)

# factories as a fixture
@pytest.fixture()
def setup4():
    def getName(name):
        if name=='list':
            return [1,2,3]
        if name=='tuple':
            return (1,2,3)
    return getName

