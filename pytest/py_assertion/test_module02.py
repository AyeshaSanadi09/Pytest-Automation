class TestClass1():
    def testType(self):
        assert type(1) == float
    def testStr(self):
        assert str.upper("Ayesha") == 'AYESHa'
    def testStr2(self):
        assert "ayesha".capitalize() == "AYESHA"