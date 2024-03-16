import pytest

def pytest_configure():
    pytest.w1 = ["sun","mon","tue"]
    pytest.w2 = ["thr","fri","sat"]

@pytest.fixture(scope="module")
def setup1():
    w1c = pytest.w1.copy()
    w1c.append("wen")
    yield w1c
    print(w1c)

@pytest.fixture()
def setup2():
    w2c = pytest.w2.copy()
    w2c.insert(0,"wen")
    yield w2c
    print(w2c)

@pytest.fixture()
def setup3(request):
    day = getattr(request.module, "w1")
    print("Fixture setup..")
    print("Fixture scope:",request.scope)
    print("Module name is:",request.module.__name__)
    print("Funcion name is:",request.function.__name__)
    day.append("wen")
    yield day

@pytest.fixture()
def setup4():
    def listType(attr):
        if attr == 'list':
            return [1,2,3]
        elif attr == 'tuple':
            return (1,2,3)
    return listType

