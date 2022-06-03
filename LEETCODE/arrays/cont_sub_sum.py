class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        """
            nums = [23,2,4,6,7], k = 6
            slow = 0
            fast = 1
            
            [23,  2,  4,  6,  7]
                  *   *
             
             2 + 4 = 6
             
            Two pointers
            slow and fast
            hold the slow pointer and use the faster one to get all 
            sub arrays and chech for the condition
            if condition is met: return True
            else: shift the slow pointer and adjust the faster one
            and repeat the process again.
            
            return False
        """
        
        if len(nums) == 1:
            return False
        
        slow = 0
        fast = 1
        
        while slow < len(nums) - 1:
            if fast < len(nums):
                sum_ = sum(nums[slow : fast + 1])
                if sum_ % k == 0:
                    return True
                fast += 1
            else:
                slow += 1
                fast = slow + 1
        
        return False