import sys
import re
from collections import Counter
from datetime import datetime

def parseGuardSleepPattern(sleepPatternText):
  match = re.match(r"\[(.*)\] (.*)", sleepPatternText)
  if not match:
    raise Exception("Cannot parse this pattern")

  event = {}
  event["date"] = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M")
  
  # [1518-11-01 00:00] Guard #10 begins shift
  beginShiftMatch = re.match(r"Guard #(\d*) begins shift", match.group(2))

  if beginShiftMatch:
    guardId = int(beginShiftMatch.group(1))

    event["type"] = "New guard"
    event["guardId"] = guardId
    return event

  # [1518-11-01 00:05] falls asleep
  fallAsleepMatch = re.match(r"falls asleep", match.group(2))

  if fallAsleepMatch:
    event["type"] = "Falls asleep"
    return event

  # [1518-11-01 00:25] wakes up
  wakesUpMatch = re.match(r"wakes up", match.group(2))

  if wakesUpMatch:
    event["type"] = "Wakes up"
    return event

  if not match:
    raise Exception("Cannot parse this pattern")

def processSleepPattens(sleepPatternEvents):
  # Sort by date
  sleepPatternEvents = sorted(sleepPatternEvents, key=lambda e: e["date"])

  guardSleepMap = {}
  guardOnDuty = -1

  i = 0
  count = len(sleepPatternEvents)

  while i < count:
    sleepEvent = sleepPatternEvents[i]
    if sleepEvent["type"] == "New guard":
      guardOnDuty = sleepEvent["guardId"]

      if not guardOnDuty in guardSleepMap:
        guardSleepMap[guardOnDuty] = Counter()

      i += 1
      continue

    if sleepEvent["type"] == "Falls asleep":
      sleepsToEvent = sleepPatternEvents[i + 1]

      assert(sleepsToEvent["type"] == "Wakes up")

      sleepsFrom = sleepEvent["date"].minute
      sleepsTo = sleepsToEvent["date"].minute

      guardSleepMap[guardOnDuty] += Counter(range(sleepsFrom, sleepsTo))

      # Handled 2 events
      i += 2
      continue

    raise Exception("Some weird event ordering thing happened")

  return guardSleepMap

def calculateMostAsleepGuard(guardSleepMap):
  # Find the guard who was sleeping the most
  (guardId, sleepCounts) = max(guardSleepMap.items(), key=lambda (k,v): sum(1 for e in v.elements()))
  [(mostCommonMinuteAsleep, count)] = sleepCounts.most_common(1)

  return (guardId, mostCommonMinuteAsleep)

def calculateMostSleptMinute(guardSleepMap):
  # Find the minute that was slept the most
  (guardId, sleepCount) = max(guardSleepMap.items(), key=lambda (k,v): [x[1] for x in v.most_common(1)])
  [(mostCommonMinute, count)] = sleepCount.most_common(1)

  return (guardId, mostCommonMinute)

if __name__ == "__main__":
  sleepPatternEvents = map(lambda c: parseGuardSleepPattern(c.strip()), sys.stdin)
  guardSleepMap = processSleepPattens(sleepPatternEvents)

  (mostAsleepGuard, mostCommonMinuteAsleep) = calculateMostAsleepGuard(guardSleepMap)
  print("Strategy 1: {}".format(mostAsleepGuard * mostCommonMinuteAsleep))

  (guardId, mostCommonMinute) = calculateMostSleptMinute(guardSleepMap)
  print("Strategy 2: {}".format(guardId * mostCommonMinute))
