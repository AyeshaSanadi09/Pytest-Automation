import pytest
from utilities.util import get_data

@pytest.mark.parametrize("a,b,c,d",get_data())
def test_checkDataFromFile(a,b,c,d):
    print(d)
