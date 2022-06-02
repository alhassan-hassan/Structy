class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        print(nums)
        nums.sort()
        max_ = 1
        
        if len(nums) < 3:
            return 
        opt1 = nums[0] * nums[1] * nums[-1]
        opt2 = nums[-1] * nums[-2] * nums[-3]
        return max(opt1, opt2)
        