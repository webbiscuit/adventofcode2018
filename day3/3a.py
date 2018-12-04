from functools import reduce
from collections import namedtuple, Counter
import re
import sys

Claim = namedtuple("Claim", "id x y width height")

def parseClaimText(claimText):
  match = re.match(r"#(\d*) @ (\d*),(\d*): (\d*)x(\d*)", claimText)
  id = int(match.group(1))
  x = int(match.group(2))
  y = int(match.group(3))
  width = int(match.group(4))
  height = int(match.group(5))

  return Claim(id, x, y, width, height)

def getLimits(claims):
  maxX = max(map(lambda c: c.x + c.width, claims))
  maxY = max(map(lambda c: c.y + c.height, claims))
  return (maxX, maxY)

def mapClaimTo1D(claim, maxX):
  results = list()
  y = claim.y

  while y < claim.y + claim.height:
    results.extend(range(claim.x + (y * maxX), claim.x + (y * maxX) + claim.width))
    y += 1

  return results

def calculateSharedFabric(claims):
  (maxX, maxY) = getLimits(claims)

  fabricMaps = map(lambda c: mapClaimTo1D(c, maxX), claims)
  fabricUsageCount = Counter(x for xs in fabricMaps for x in xs)

  # 112418
  count = reduce(lambda result, c: result + 1 if c > 1 else result, fabricUsageCount.values(), 0)
  
  return count

if __name__ == "__main__":
  claims = map(lambda c: parseClaimText(c.strip()), sys.stdin)
  sharedFabric = calculateSharedFabric(claims)
  print(sharedFabric)