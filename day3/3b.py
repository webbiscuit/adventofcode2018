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

def findUniqueClaimInFabric(fabricUsageCount, claims, maxX):
  uniqueFabric = set(k for (k,v) in fabricUsageCount.items() if v == 1)  

  for claim in claims:
    mappedClaim = set(mapClaimTo1D(claim, maxX))
    if (mappedClaim.issubset(uniqueFabric)):
      return claim

  return None

def findUniqueClaim(claims):
  (maxX, maxY) = getLimits(claims)

  fabricMaps = map(lambda c: mapClaimTo1D(c, maxX), claims)
  fabricUsageCount = Counter(x for xs in fabricMaps for x in xs)

  # Loop through all the claims and find out which fits with all the 1s
  claim = findUniqueClaimInFabric(fabricUsageCount, claims, maxX)
  print(claim)
 
  return claim

if __name__ == "__main__":
  claims = map(lambda c: parseClaimText(c.strip()), sys.stdin)
  claim = findUniqueClaim(claims)
  print(claim.id)