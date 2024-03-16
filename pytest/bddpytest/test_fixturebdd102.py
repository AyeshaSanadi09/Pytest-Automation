from pytest_bdd import scenario, given, when, then, scenarios
from pathlib import Path
import pytest

featureFileDir = 'myfeatures'
featureFile = 'fixture.feature'

BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

scenarios(FEATURE_FILE)

@pytest.fixture()
def setup_set():
    print("\n In fixture... setup() function...\n")
    c = {"America","India","Poland","UK"}
    return c;

@given("A datatpe set")
def checkType(setup_set):
    print("In background")
    if not isinstance(setup_set,set):
        pytest.xfail("Type is not a set")

@given("the set is not empty")
def setNotEmpty(setup_set):
    if len(setup_set) == 0:
        pytest.xfail("empty set")


@given("a set of 3 elements",target_fixture="c1")
def setOfEle(setup_set):
    if len(setup_set) == 0:
        pytest.xfail("The set is empty")
    elif len(setup_set) >3:
        while len(setup_set) >3:
            setup_set.pop()
    return setup_set

@when("add 2 element to the set")
def add_ele(c1):
    c1.add("Israil")
    c1.add("Germany")

@then("the set should have 5 elements")
def finalSet(c1):
    print(c1)
    assert len(c1) == 5
