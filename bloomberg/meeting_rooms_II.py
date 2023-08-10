class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([x[0] for x in intervals])
        end = sorted([x[1] for x in intervals])

        p1 = p2 = 0
        count = res = 0

        while p1 < len(start):
            if start[p1] < end[p2]:
                count += 1
                p1 += 1
            else:
                p2 += 1
                count -= 1

            res = max(res, count)

        return res
