import sys
import re
from collections import Counter
from datetime import datetime

def processReaction(polymer):
  indices = range(0, len(polymer))

  while True:
    newIndices = [] 

    i = 0
    count = len(indices)

    while i < count:
      if i == count - 1:
        # Last one gets added automatically
        newIndices.append(indices[i])
        i += 1
      else:
        ix1 = indices[i]
        ix2 = indices[i + 1]

        if (abs(ord(polymer[ix1]) - ord(polymer[ix2])) != 32):
          # Okay, keep this one for now
          newIndices.append(ix1)
          i += 1
        else:
          # Not good, don't add either
          i += 2

    newPolymer = ''

    if len(newIndices) == len(indices):
      break

    # Go again
    indices = newIndices

  for ix in newIndices:
    newPolymer += polymer[ix]

  return newPolymer
    

def optimisePolymerLength(basePolymer):
  minLength = len(basePolymer)

  # Loop through a-z
  for c in map(chr, range(ord('a'), ord('z') + 1)):
    c2 = chr(ord(c) - 32)
    newPolymer = basePolymer.replace(c, '')
    newPolymer = newPolymer.replace(c2, '')
    
    minLength = min(len(processReaction(newPolymer)), minLength)

  return minLength

if __name__ == "__main__":
  polymer = sys.stdin.readline()
  newPolymer = processReaction(polymer)

  print(len(newPolymer))

  smallestPolymer = optimisePolymerLength(newPolymer)
  print(smallestPolymer)
  