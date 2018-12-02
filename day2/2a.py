from collections import Counter
import sys

def calculateChecksum(boxIds):
    a = 0
    b = 0

    for boxId in boxIds:
        characterSeenCount = Counter(boxId)

        if 2 in characterSeenCount.values():
            a += 1

        if 3 in characterSeenCount.values():
            b += 1

    return a * b


if __name__ == "__main__":
    boxIds = map(lambda s: s.strip(), sys.argv[1:])    
    checksum = calculateChecksum(boxIds)
    print(checksum)