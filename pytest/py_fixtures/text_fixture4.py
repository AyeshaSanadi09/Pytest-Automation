#fixture sharing
import pytest

def testWeekdays1(setup1):
    assert setup1 == ["sun","mon","tues","wen"]

def testWeekdays2(setup2,setup1):
    assert len(setup2) == len(setup1)
