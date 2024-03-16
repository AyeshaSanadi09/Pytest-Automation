import pytest

pytestMarker = [pytest.mark.str, pytest.mark.smoke]

@pytest.mark.salinity
def testStr1():
        num = 9/4
        str1 = "hii i am"+" Ayesha"
        assert str(9/4) == '2.25'
        assert str1 == "hii i am Ayesha"
        assert str1+str(9/4) == "hii i am Ayesha2.25"

@pytest.mark.salinity
def testStr2():
    str2="abcdefghijklmnopqrstuvwxyz"
    assert len(str2) == 26

@pytest.mark.salinity
@pytest.mark.unity
def testStr3():
    str3 = "abcdefghijklmnopqrstuvwxyz"
    assert str3[0] == 'a'
    assert str3[-1] == 'z'

def testStrslice():
    str4 = "abcdefghijklmnopqrstuvwxyz"
    assert str4[:] == "abcdefghijklmnopqrstuvwxyz"
    assert str4[-3:] == "xyz"
    assert str4[:21:5] == "afkpu"

def testStrsplit():
    str5="python, pytest and automation"
    assert str5.split() == ["python,", "pytest","and","automation"]

