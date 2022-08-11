from collections import Counter
class Solution:
    def findAnagrams(self, s, p) :
        
        sl = 0
        ana =[]
        
        p_counter = Counter(p)
        s_counter = Counter()
        
        for i in range(len(s)):
            s_counter[s[i]] += 1
            
            if i >= len(p):
                if s_counter[sl] == 1:
                    s_counter.pop(s[sl])
                else:
                    s_counter[s[sl]] -= 1
                sl += 1
            
            if s_counter == p_counter:
                ana.append(sl)
                    
        return ana
                    
            
            
        