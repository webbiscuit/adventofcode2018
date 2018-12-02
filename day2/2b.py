from functools import reduce
import sys

def calculateDistances(id, otherIds):
    distances = dict()

    for otherId in otherIds:
        distance = 0
        for (c1, c2) in zip(id, otherId):
            if c1 != c2:
                distance += 1

        distances[otherId] = distance

    return distances

def findCommonString(id, otherId):
    commonId = ''

    for (c1, c2) in zip(id, otherId):
        if c1 == c2:
            commonId += c1

    return commonId

def findCommonBoxIds(boxIds):

    i = 0

    while i < len(boxIds):
        distances = calculateDistances(boxIds[i], boxIds[i:])

        # Only interested in exactly 1
        for k, v in distances.items():
            if v == 1:
                a = boxIds[i]
                b = k

                return findCommonString(a, b)

        i += 1




if __name__ == "__main__":
    boxIds = sys.argv[1:]
    commonIds = findCommonBoxIds(boxIds)
    print(commonIds)