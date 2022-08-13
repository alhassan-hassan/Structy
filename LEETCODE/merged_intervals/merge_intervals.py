class Solution:
    def merge(self, interval):
        """
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        
        check to see whether there is an intersection.
        If there's,
            adjust the window before appending
        Else:
            you continue to append the current value
        """
        
        #### THEIRS
        
        N = len(interval)
        interval.sort()
        res = []
        
        for i in range(N):
            if i == 0 or res[-1][1] < interval[i][0]:
                res.append(interval[i])
                
            else:
                res[-1][1] = max(res[-1][1], interval[i][1])
                
        return res
        
        
        
        #### MINE
#         if N <= 1:
#             return interval
        
#         res = []
#         interval.sort()
#         for i in range(N):
#             if i == 0:
#                 res.append(interval[i])
                
#             else:
#                 x_cor1, y_cor1 = res[-1]
#                 x_cor2, y_cor2 = interval[i]
                
#                 max_ = max(x_cor1, x_cor2)
#                 min_ = min(y_cor1, y_cor2)
                
#                 if max_ <= min_:
#                     res[-1] = [min(x_cor1, x_cor2), max(y_cor1, y_cor2)]
#                 else:
#                     res.append(interval[i])
                    
#         return res
                
                
                
        
        
        
        