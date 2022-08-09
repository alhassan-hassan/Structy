class Solution:
    def intervalIntersection(self, firstList, secondList):
        """
        [[0,2] , [5,10] , [13,23] , [24,25]]
                    *
        
        [[1,5] , [8,12] , [15,24] , [25,26]]
                    *
        
        [[1,2] , [5,5] , [8,10] , [15,23] , [24,24] , [25,25]]
        
        max of two values = 1
        min = 2     inter = [1, 2]
        
        
        max = 5,  min = 5   inter = [5, 5]
        
        
        
        [8, 20] 
           *
                    max = 8
        [1, 5]
           *
           
           8 > 5
        """
        
        if len(firstList) == 0 or len(secondList) == 0:
            return []
        
        p1 = p2 = 0
        fl, sl = firstList, secondList
        ans = []
        
        while p1 < len(fl) and p2 < len(sl):
            max_ = max(fl[p1][0], sl[p2][0])
            min_ = min(fl[p1][1], sl[p2][1])
            
            if max_ <= min_:
                ans.append([max_, min_])
            
            if fl[p1][1] > sl[p2][1]:
                p2 += 1
                
            else:
                p1 += 1
                
        return ans
                