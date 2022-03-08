from collections import defaultdict
import math
def fre(s):
    dic1 = defaultdict(int)
    for char in s:
        dic1[char] += 1

    max = ""
    fre = float("-inf")

    for char in s:
        if dic1[char] > fre:
            max = char
            fre = dic1[char]

    return max

print(fre())


# STRUCTY
def most_frequent_char(s):
  count = {}
  for char in s:
    if char not in count:
      count[char] = 0    
    count[char] += 1
    
  best = None
  for char in s:
    if best is None or count[char] > count[best]:
      best = char
  return best

from collections import Counter

def most_frequent_char(s):
  count = Counter(s)
  best = None
  for char in s:
    if best is None or count[char] > count[best]:
      best = char
  return best