class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count0 = 0
        maxOnes = 0
        
        if len(nums) == 0:
            return 0
        
        slow = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count0 += 1
                
            while count0 > 1:
                if nums[slow] == 1:
                    slow += 1
                else:
                    slow += 1
                    count0 -= 1
            maxOnes = max(maxOnes, i - slow + 1)
                    
        return maxOnes
                    
                    