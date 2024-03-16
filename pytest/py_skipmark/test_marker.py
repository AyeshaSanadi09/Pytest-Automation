import pytest

# definening marker globally
pytestmark = [pytest.mark.Smoke, pytest.mark.Strtest]

@pytest.mark.Sanity
def testStr():
    str1 = "ayesha"
    assert str1[0] == 'a'
    assert str1[5] == 'a'

def testStr2():
    str2 = "fija"
    assert str2 == "fija"

def testStrSplit3():
    str3 = "abcdefghijklmnopqrstuvwxyz"
    assert str3[-3:] == "xyz"
    assert str3[1:5] == 'bcde'
    assert str3[::2] == 'acegikmoqsuwy'

def testStrJoin4():
    str4 = "python,pytest and automation"
    assert str4.split() == ['python,pytest','and','automation']
    assert str4.split(',') == ['python','pytest and automation']

@pytest.mark.Str
@pytest.mark.Sanity
def testStrLen5():
    str5 = 'hii ayesha'
    assert len(str5) == 10

@pytest.mark.Sanity
def testStr6():
    str6 = "hii"
    str62 = ' ayesha'
    assert str6+str62 == 'hii ayesha'
    assert str6+' alita' == 'hii alita'