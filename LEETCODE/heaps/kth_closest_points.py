from collections import defaultdict
class Solution:
    def kClosest(self, points, k):
        def distance(arr):
            return arr[0] ** 2 + arr[1] ** 2
        
        myH = []
        hmap = defaultdict(list)
        res = []
        
        for i in range (len(points)):
            dis = distance(points[i])
            heapq.heappush(myH, (dis * -1, points[i]))
            if i >= k:
                heapq.heappop(myH)
        for dis in myH:
            res.append(dis[1])
            
        return res
        
        
        
        