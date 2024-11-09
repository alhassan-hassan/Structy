import heapq
class Solution:
    def minMeetingRooms(intervals):
        heap = []
        intervals.sort(key = lambda x: x[0])

        for interval in intervals:
            start, end = interval
            if heap and start >= heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, end)

        return len(heap)
    
# run the solution code
# intervals = [[0, 30], [5, 10], [15, 20]]
intervals = [[7, 10], [2, 4]]
test = Solution.minMeetingRooms(intervals)
print(test)

            

        # start = sorted([x[0] for x in intervals])
        # end = sorted([x[1] for x in intervals])

        # p1 = p2 = 0
        # count = res = 0

        # while p1 < len(start):
        #     if start[p1] < end[p2]:
        #         count += 1
        #         p1 += 1
        #     else:
        #         p2 += 1
        #         count -= 1

        #     res = max(res, count)

        # return res