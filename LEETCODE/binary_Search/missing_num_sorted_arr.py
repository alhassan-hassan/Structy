class Solution:
    def missingElement(self, nums, k):
        # using binary search
        
        def missing(ind):
            return nums[ind] - nums[0] - ind
        
        lo, hi = 0, len(nums)
        
        while lo < hi:
            mid = (lo + hi) // 2
            
            if missing(mid) < k:
                lo = mid + 1
            else:
                hi = mid
                
        return nums[lo - 1] + k - missing(lo - 1)
        
#         start = nums[0] + 1
#         seen = set(nums)
#         missing = None
        
#         while k > 0:
#             if start not in seen:
#                 missing = start
#                 k -= 1
                
#             start += 1
            
#         return missing
            
            
        
        