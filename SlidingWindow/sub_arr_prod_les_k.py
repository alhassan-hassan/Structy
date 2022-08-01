class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        
        """
        [10, 5 , 2 , 6], k = 100
             *         
                     *
        10   counter = 0 - 0 + 1 = 1
        10, 5, counter = 1 + 1 - 0 + 1 = 3
        10, 5, 2 => remove 10
        5, 2, counter = 3 + 2-1 + 1 = 5
        5, 2, 6, counter = 5 + 3-1 + 1 = 8
        """
        if k <= 1:
            return 0
        
        counter = 0
        prod = 1
        left = 0
        right = 0
        
        while right < len(nums):
            prod *= nums[right]
            print(prod)
            
            while prod >= k:
                prod /= nums[left]
                left += 1
                
            counter += right - left + 1
            
            right += 1
        return counter
        
        