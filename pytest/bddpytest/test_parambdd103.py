from pytest_bdd import scenario, given, when, then, scenarios, parsers
from pathlib import Path
import pytest

featureFileDir = 'myfeatures'
featureFile = 'parameterizing.feature'

BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

scenarios(FEATURE_FILE)

@given("there are 3 varities of fruits",target_fixture="fruits")
def existingFruits():
    fruits = {"apple","grapes","strawberrrry"}
    return fruits

@when("we add a same varity of fruit")
def add_ele(fruits):
    fruits.add("apple")

@then("there is same count of varities")
def sameCount(fruits):
    assert len(fruits) == 3

@then("if we add a different varity of fruit")
def add_newele(fruits):
    fruits.add("mango")

@then(parsers.parse("the count of varities increases to {count:d}"))
def finalCount(fruits,count):
    print(fruits)
    assert len(fruits) == count

@given(parsers.parse("Given there are {count1:d} fruits"),target_fixture='startFruit')
def existing_fruits(count1):
    return dict(start=count1,eat=0)

@when(parsers.parse("I eat {eat:d} fruit"))
def eat_fruits(startFruit,eat):
    print(startFruit)
    startFruit["eat"]+=eat

@then(parsers.parse("I should have {left:d} fruits"))
def left_fruits(startFruit,count1,left):
    assert startFruit['start'] == count1
    assert count1 - startFruit['eat'] == left
