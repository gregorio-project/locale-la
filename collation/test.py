#!/usr/bin/env python3

from icu import RuleBasedCollator
from sys import exit

RULES = ''
with open ("rules.txt", "r") as rulesfile:
    RULES=rulesfile.read()

COLLATOR = RuleBasedCollator(RULES)

EXIT_CODE = 0

# Very simple test function: we 
def testOrder(argList, testName):
    global EXIT_CODE
    argList = argList.split(' ')
    newList = sorted(argList, key=COLLATOR.getSortKey)
    if argList != newList:
        EXIT_CODE = 1
        print(testName+' ... FAIL!')
        print("expected ["+(", ".join(argList))+"]")
        print("got      ["+(", ".join(newList))+"]")
    else:
        print(testName+' ... OK')

testOrder("a ad ae æ af b", "basic æ")
testOrder("o od oe œ of q", "basic œ")
testOrder("a ad ae æ ǽ af b", "accented æ")
testOrder("a á b", "accented a")
testOrder("o ó œ œ́ p", "accented œ")
testOrder("ă ä ā ĕ ë ē ĭ ï ī ñ ŏ ö ō ŭ ü ū ў ÿ ȳ z", "length accents")

exit(EXIT_CODE)
