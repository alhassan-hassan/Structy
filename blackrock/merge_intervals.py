class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in range(len(intervals)):
            last = res[-1]
            if intervals[i][0] <= last[1]:
                res[-1][1] = max(intervals[i][1], last[1])
            else:
                res.append(intervals[i])


        return res