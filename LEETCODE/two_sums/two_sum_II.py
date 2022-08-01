class Solution:
    def twoSum(self, nums, target):
        
        """
        [2, 7 , 1 1 , 15]
         *
                      *
        summ greater, reduce fast pointer
        summ less, increase the right pointer
        same, return the indices of the two numbers => return the two pointers
        
        Runtime: Time = O(n)
                 Space = 0(1)
                 
        """
        if len(nums) < 2:
            return []
        
        sl = 0
        fast = len(nums) - 1
        res = []
        
        while sl < fast:
            summ = nums[sl] + nums[fast]
            if summ > target:
                fast -= 1
            elif summ < target:
                sl += 1
            else:
                res.extend([sl+1, fast+1])
                return res
        return res
                