class Solution:
    def lengthOfLongestSubstring(self, s):
        sub = sl = 0
        hmap = {}
        for i in range(len(s)):
            while s[i] in hmap:
                hmap.pop(s[sl])
                sl += 1
            hmap[s[i]] = "There"
            
            sub = max(sub, i - sl + 1)
            
        return sub
                
            
        