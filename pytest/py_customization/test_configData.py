from utilities.myconfigparser import *
from utilities.ConfigFileParser import ConfigFileParser

config = ConfigFileParser("qa.ini")

def test_getGmailUrl():
    print(getGmailUrl())

def test_getGmailPass():
    print(getGmailPass())