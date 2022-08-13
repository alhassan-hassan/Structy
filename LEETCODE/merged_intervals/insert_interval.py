class Solution:
    def insert(self, intervals, newInterval):
        N = len(intervals)
        
        if N == 0:
            return [newInterval]
        
        finale = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                finale.append(newInterval)
                return finale + intervals[i : ]
            
            elif intervals[i][1] < newInterval[0]:
                finale.append(intervals[i])
                
            else:
                x_cor = min(newInterval[0], intervals[i][0])
                y_cor = max(newInterval[1], intervals[i][1])
                
                newInterval = [x_cor, y_cor]
                
        finale.append(newInterval)
        
        return finale
                