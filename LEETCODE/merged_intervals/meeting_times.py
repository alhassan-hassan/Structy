class Solution:
    def minMeetingRooms(self, intervals):
        """
        [ [2,15] , [4,9] , [9,29] , [16,23] , [36,45] ]
        
        [[4, 9] [9, 29], ]
                     2
            
        """
        N, count, res = len(intervals), 0, 0
        
        if N == 0:
            return 0
        
        p1 = p2 = 0
        
        intervals.sort()
        
        start = []        
        end = []
        
        start = sorted([i[0] for i in intervals])
        end = sorted(i[1] for i in intervals)
        
        while p1 < len(intervals):
            if start[p1] < end[p2]:
                count += 1
                p1 += 1
            else:
                count -= 1
                p2 += 1
                
            res = max(res, count)
                
        return res
