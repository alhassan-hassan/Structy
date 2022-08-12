from collections import Counter 
class Solution:
    def minWindow(self, s, t) :
        if len(t) == 0 or len(t) > len(s): return ""
        if s == t: return s
        
        s_counter = Counter()
        t_counter = Counter(t)
        
        ind, indLen, lo =  [-1, -1], float("inf"), 0
        have, need = 0, len(t_counter)
        
        for i in range(len(s)):
            c = s[i]
            s_counter[c] += 1

            if c in t_counter and t_counter[c] == s_counter[c]:
                have += 1
                    
            while have == need:
                s_counter[s[lo]] -= 1
                if i - lo + 1 < indLen:
                    indLen = i - lo + 1
                    ind = [lo, i]
                if s[lo] in s_counter and s_counter[s[lo]] < t_counter[s[lo]]:
                    have -= 1
                lo += 1
        left, right = ind
        
        return s[left : right + 1] if indLen != float("inf") else ""
                