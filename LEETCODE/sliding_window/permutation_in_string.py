from collections import Counter
class Solution:
    def checkInclusion(self, s1, s2):
        """
        "e i d b a o o o"      ab
         *
         
        """
        
        
#         {
#             a = 1,  *
#             b = 1   *
#         }
        
        if len(s1) > len(s2):
            return False
        
        s1_counter = Counter(s1)
        s2_counter = Counter()
        
        for i in range(len(s2)):
            s2_counter[s2[i]] += 1
            
            if i >= len(s1):
                if s2_counter[s2[i - len(s1)]] == 1:
                    s2_counter.pop(s2[i - len(s1)])
                else:
                    s2_counter[s2[i - len(s1)]] -= 1
            if s2_counter == s1_counter:
                return True
            
        return False