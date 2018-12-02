from functools import reduce
import sys

def calculateFrequencyDrift(frequencies):
    return reduce((lambda x, y: x + y), frequencies)

if __name__ == "__main__":
    frequencies = map(int, sys.argv[1:])
    drift = calculateFrequencyDrift(frequencies)
    print(drift)