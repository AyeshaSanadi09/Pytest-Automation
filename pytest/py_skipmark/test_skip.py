import sys
import pytest
# skipping whole module
pytestskip = pytest.mark.skipif(sys.platform == 'win32', reason="this is not run in windows system")

const = 9/5
def cetToFar(sel):
    return (sel*const)+32
print(cetToFar(5))

# default skip
@pytest.mark.skip(reason="for demo purpose")
def testDo1():
    assert type(const) == float

# skip based on if stmt
@pytest.mark.skipif(sys.version_info < (3,6), reason="the version is not used")
def testDo2():
    assert cetToFar(5) == 41

@pytest.mark.skipif(pytest.__version__ < '8.0', reason="plz pytest upgrade")
def testDo3():
    assert cetToFar(5) == 41.0

