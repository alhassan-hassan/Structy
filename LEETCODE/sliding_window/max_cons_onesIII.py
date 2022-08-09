class Solution:
    def longestOnes(self, nums, k):
        """
            [0, 0 , 1 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 , 1 , 0 , 0 , 0 , 1 , 1 , 1 , 1]   - k = 3
                                *
                                                                *
        """
        count0 = 0
        maxOnes = 0
        
        if len(nums) == 0:
            return 0
        
        slow = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count0 += 1
                
            while count0 > k:
                if nums[slow] == 1:
                    slow += 1
                else:
                    slow += 1
                    count0 -= 1
            maxOnes = max(maxOnes, i - slow + 1)
            
        return maxOnes
                
        
        