import sys

def calculateFrequencyCalibration(frequencies):
    frequenciesSeen = set()
    total = 0

    while True:
        for f in frequencies:
            total += f
            if total in frequenciesSeen:
                return total
            frequenciesSeen.add(total)


if __name__ == "__main__":
    frequencies = map(int, sys.argv[1:])
    calibration = calculateFrequencyCalibration(frequencies)
    print(calibration)