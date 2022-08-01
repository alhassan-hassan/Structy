class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
       
        if len(nums) <= 1:
            return 0
        
        numsClone = nums.copy()
        numsClone.sort()
        
        beg = len(nums) - 1
        end = 0
        
        print(numsClone, nums)
        for i in range(len(nums)):
            if nums[i] != numsClone[i]:
                beg = min(beg, i)
                end = max(end, i)
        
        return end - beg + 1 if end - beg >= 0 else 0