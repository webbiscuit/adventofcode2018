from functools import reduce
import sys

def buildCommonString(a, b):
    commonId = reduce(lambda result, (c1, c2): result + c1 if c1 == c2 else result, zip(a,b), '')
    return commonId

def calculateDistance(a, b):
    distance = reduce(lambda total, (c1, c2): total + 1 if c1 != c2 else total, zip(a,b), 0)
    return distance

def findCommonBoxIds(boxIds):
    for i in range(len(boxIds)):
        for j in range(i + 1, len(boxIds)):
            a = boxIds[i]
            b = boxIds[j]

            distance = calculateDistance(a, b)

            if distance == 1:
                return buildCommonString(a, b)

if __name__ == "__main__":
    boxIds = map(lambda s: s.strip(), sys.argv[1:])
    commonIds = findCommonBoxIds(boxIds)
    print(commonIds)