from collections import Counter, defaultdict

# MY IMPLEMENTATION
def anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    dic1 = defaultdict(int)

    for char in s1:
        dic1[char] += 1
    
    for char in s2:
        if not dic1[char]:
            return False

        if dic1[char] >= 1:
            dic1[char] -= 1
        else:
            return False
    return True

print(anagrams('paper', 'reapa'))


# HIS
""""
    n = length of string 1
    m = length of string 2
    Time: O(n + m)
    Space: O(n + m)
"""
def anagrams(s1, s2):
  return char_count(s1) == char_count(s2)

def char_count(s):
  count = {}
  
  for char in s:
    if char not in count:
      count[char] = 0
    count[char] += 1
  
  return count


def anagrams(s1, s2):
  return Counter(s1) == Counter(s2)