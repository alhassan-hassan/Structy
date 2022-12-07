import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) < 2:
            return len(s) - 1

        dic = collections.OrderedDict()

        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
        
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1

        # OR
        count = collections.Counter(s)
        print(count)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1