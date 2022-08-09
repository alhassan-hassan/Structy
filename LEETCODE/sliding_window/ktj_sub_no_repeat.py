class Solution:
    def numKLenSubstrNoRepeats(self, s, k):
        """
        "h a v e f u n o n l e e t c o d e",       k = 5
               *
                     *
                   
        hmap = {
            t, c, o, d, e
        
        }
        
        count = 6
        
        time = O(n)
        space = O(n)
        """
        
        hmap = {}
        count = lo = 0
        
        if len(s) < k:
            return 0
        
        for i in range(len(s)):
            while s[i] in hmap:
                hmap.pop(s[lo])
                lo += 1
                
            hmap[s[i]] = "There"
            
            if i - lo + 1 == k:
                hmap.pop(s[lo])
                lo += 1
                count += 1
                
        return count
            