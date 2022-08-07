class Solution:
    def maxSubArray(self, nums):
        # BRUTEFORCE
#         max_ = float("-inf")
#         for i in range(len(nums)):
#             curM = 0
#             for j in range(i, len(nums)):
#                 curM += nums[j]
#                 max_ = max(curM, max_)
                
#         return max_
    
        # USING KADANE'S ALGORITHM
        
        max_ = nums[0]
        curSum = 0
        
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            max_ = max(max_, curSum)
            
        return max_
        