from pytest_bdd import scenario, given, when, then, scenarios, parsers
from pathlib import Path
import pytest

featureFileDir = 'myfeatures'
featureFile = 'scenarioOutline.feature'

BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

@scenario(FEATURE_FILE,"Scene Outline test")
def test_outline():
    pass

@given(parsers.parse("there are {start:d} cucumbers"),target_fixture="cucumbers")
def existingCucumbers(start):
    return dict(start=start)

@when(parsers.parse("I deposit {deposit:d} cucumbers"))
def depositeCucumbers(cucumbers,deposit):
    cucumbers['deposit'] = deposit
    print(cucumbers)

@when(parsers.parse("I withdraw {withdraw:d} cucumbers"))
def withdrawCucumbers(cucumbers,withdraw):
    cucumbers['withdraw'] = withdraw
    print(cucumbers)

@then(parsers.parse("I should have {final:d} cucumbers"))
def finalCucumbers(cucumbers,final):
    assert cucumbers['start']+cucumbers['deposit']-cucumbers['withdraw'] == final
