import collections
class Solution:
    def maxSlidingWindow(self, nums, k):
        N = len(nums)
        
        if N * k == 0:
            return []
        
        if N == 1:
            return nums
        
        l = r = 0
        res, dq = [], collections.deque()
        
        while r < N:
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            
            if l > dq[0]:
                dq.popleft()
                
            if r  >= k-1:
                res.append(nums[dq[0]])
                l += 1
                
            r += 1
                
        return res
        
        
        