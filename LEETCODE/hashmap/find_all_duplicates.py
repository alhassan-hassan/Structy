class Solution:
    def findDuplicates(self, nums):
        # THE DOUBLE NEGATION TECHNIQUE
        
        count = []
        
        for i in range(len(nums)):
            ind = abs(nums[i]) - 1
            
            if nums[ind] < 0:
                count.append(abs(nums[i]))
                
            else:
                nums[ind]  = nums[ind] * -1
                
        return count
        