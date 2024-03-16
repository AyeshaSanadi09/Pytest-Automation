def testFactoriesAsFix(setup4):
    assert type(setup4('list')) == list
    assert type(setup4('tuple')) == tuple
