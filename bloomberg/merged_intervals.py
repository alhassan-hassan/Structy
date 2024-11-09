class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        for i in range(len(intervals)):
            if i == 0 or res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])

        return res
    
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        stack = []

        for interval in intervals:
            if not stack or interval[0] > stack[-1][1]:
                stack.append(interval)
            else:
                stack[-1][1] = max(stack[-1][1], interval[1])
        return stack

        # if not intervals:
        #     return intervals

        # intervals.sort()
        # res = [intervals[0]]

        # for i in range(len(intervals)):
        #     last = res[-1]
        #     if last[1] >= intervals[i][0]:
        #         res[-1][1] = max(last[1], intervals[i][1])

        #     else:
        #         res.append(intervals[i])

        # return res
        