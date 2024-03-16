from pytest_bdd import scenario, given, when, then, scenarios
from pathlib import Path
import pytest

featureFileDir = 'myfeatures'
featureFile = 'first101.feature'

BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

scenarios(FEATURE_FILE)

def pytest_configure():
    pytest.AMT = 0 #global variable

# @scenario(FEATURE_FILE,"Withdrawal of money")
# def test_withdrawal():
#     print("End of withdrwal test")
#     pass

@given("the account balance is 100")
def current_balance():
    pytest.AMT = 100

@when("the account holder withdraws 30")
def withdraw_amount():
    pytest.AMT = pytest.AMT-30

@then("the account balance should be 70")
def finalBalance():
    assert pytest.AMT ==70

# @scenario(FEATURE_FILE,"Removal of items from set")
# def test_getList():
#     print("End of getList test")
#     pass

@given("a set of 3 fruits",target_fixture="myset")
def current_set():
    myset = {"Mango","Apple","Orange"}
    return myset

@when("we remove a fruit from the set")
def remove_fruit(myset):
    myset.pop()
    print(myset)

@then("the set will have 2 fruits")
def finalSet(myset):
    assert len(myset) ==2
