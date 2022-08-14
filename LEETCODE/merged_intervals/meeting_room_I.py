class Solution:
    def canAttendMeetings(self, intervals):
        
        # MINE
        N = len(intervals)
        if N <= 1:
            return True
        
        intervals.sort()
        
        
        for i in range(1, N):
            max_ = max(intervals[i - 1][0], intervals[i][0])
            min_ = min(intervals[i - 1][1], intervals[i][1])
            
            if max_ < min_:
                return False
            
        return True
        
        # THEIRS
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True
        
        