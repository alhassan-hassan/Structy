class Solution:
    def firstMissingPositive(self, nums):
        
        # NOW THE MAGIC WHERE MEMORY SPACE IS BEATEN TO CONSTANT TIME
        """
        1. the missing number will always belong to 1--- len(nums) + 1
        2. Use the inputr array as extra memory
        3. Three loops
            i.   1st loop: Change all negatives to zeroes
            ii.  Do the negation technique to identify the indices changed
            iii. Now trace to see if a particular index is missing then that indes is
                 the missing positive number. Else return return len(of the array)
        """
        if len(nums) == 1:
            return 1 if nums[0] != 1 else 2
        
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = nums[i] * 0
                
        for i in range(len(nums)):
            ind = abs(nums[i]) - 1
            if ind >= 0 and ind < len(nums):
                if nums[ind] == 0:
                    nums[ind] = -(len(nums) + 1)
                else:
                    nums[ind]  = abs(nums[ind]) * -1
       
    
        for i in range(1, len(nums) + 1):
            if nums[i-1] >= 0:
                # print(nums[i-1], i)
                return i
        
        return len(nums) + 1
                
        
            
                
        
        
        # BUT WE REQUIRE A CONSTANT SPACE ALGORITHM
#         dic = {}
        
#         for num in nums:
#             if num not in dic:
#                 dic[num] = "R"
                
#         for num in range(1, max(nums) + 1):
#             if num not in dic:
#                 return num
            
#         if max(nums) <= 0:
#             return 1
#         return max(nums) + 1
        