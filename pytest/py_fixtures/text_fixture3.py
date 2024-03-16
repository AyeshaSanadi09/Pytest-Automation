import os
import pytest

fileName="demoFile.txt"

@pytest.fixture()
def setup():
    f = open(fileName,'w')
    f.write("hii this is my file")
    f.close()
    f = open(fileName,'r+')
    yield f # after yeild statement the remaining code is worked as teardown
    f.close()
    os.remove(fileName)

def testFile(setup):
    assert setup.readline() == "hii this is my file"

weekdays1 = ["sun","mon","tues"]
weekdays2 = ["thrs","fri","sat"]

@pytest.fixture()
def setup1():
    print("setup method called...")
    weekdays1.append("wen")
    yield weekdays1
    print("value is return from setup1 method")
    weekdays1.pop()

@pytest.fixture()
def setup2():
    print("setup2 method called...")
    weekdays2.insert(0,"wen")
    yield weekdays2
    print("value is return from setup2 method")
    weekdays2.pop()

def testWeekdays1(setup1):
    assert setup1 == ["sun","mon","tues","wen"]

def testWeekdays2(setup2,setup1):
    assert len(setup2+weekdays1) == len(setup1+weekdays2)
