import pytest

QA = "qa.prop"
Prod = "prod.prop"

# hooks define
def pytest_addoption(parser):
    parser.addoption('--cmdopt',default='QA')


@pytest.fixture()
def cmdOpt(pytestconfig):
    print("\nInside fixture")
    opt = pytestconfig.getoption("cmdopt")
    if opt == 'Prod':
        f = open(Prod,"r")
    else:
        f = open(QA,'r')
    yield f


