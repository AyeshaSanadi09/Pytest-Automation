import pytest
import  os

w1=["sun","mon","tue"]
w2=["thr","fri","sat"]
fileName = "file.txt"

@pytest.fixture()
def setup01():
    w1.append("wen")
    yield w1
    print("\n inside fixture 1..")
    w1.pop()

@pytest.fixture()
def setup02():
    w2.insert(0,"wen")
    yield w2
    print("\n inside fixture 2..")
    w2.pop()

@pytest.fixture()
def setup03():
    f = open(fileName,'w')
    f.write("Hii, Ayesha Sanadi")
    f.close()
    f = open(fileName,'r+')
    yield f
    print("\n inside fixture 3..")
    f.close()
    os.remove(fileName)

def test_list(setup01):
    setup01.extend(w2)
    assert setup01 == ["sun","mon","tue","wen","thr","fri","sat"]

def test_list2(setup01,setup02):
    assert len(setup01+w2) == len(setup02+w1)

def test_file(setup03):
    assert setup03.readline() == "Hii, Ayesha Sanadi"