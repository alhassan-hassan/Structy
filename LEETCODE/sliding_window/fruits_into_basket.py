from collections import defaultdict
class Solution:
    def totalFruit(self, fruits):
        if len(fruits) < 3:
            return len(fruits)
        
        fruL = 0
        sl = hi = track = count = 0
        hmap = defaultdict(int)
        
        while hi < len(fruits):
            if fruits[hi] not in hmap:
                track += 1
            hmap[fruits[hi]] += 1
            count += 1
            
            while track > 2:
                count -= 1
                if hmap[fruits[sl]] == 1:
                    hmap.pop(fruits[sl])
                    track -= 1
                else:
                    hmap[fruits[sl]] -= 1
                sl += 1
                
            fruL = max(fruL, count)
            hi += 1
            
        return fruL
            
                    
            
            