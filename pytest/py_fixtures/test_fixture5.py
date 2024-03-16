import pytest

months = ['Jan','Feb','March']

def testCheckRequest1(setup3):
    assert len(setup3) == 5
    assert "May" in setup3

