class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        nums = [0, 1 , 0 , 3 , 12]      Output: [1 , 3 , 1 2 , 0 ,0]
                s  p
                
               [1, 0 , 0 , 3 , 12]
                   s       p
                   
               [1, 3 , 0 , 0 , 12]
                m s       p
                      
                
        [1, 0 , 1]
            s   f
        """
         
        #OPTIMAL SOLUTION
        
        if len(nums) <= 1:
            return nums
       
        p1 = 0
        p2 = 0
        while p2 < len(nums):
            if nums[p1] != 0:
                p1 += 1
                p2 = p1 + 1
            elif nums[p2] == 0:
                p2 += 1
                print(p2)
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 += 1
                
            
        
        # NOT BAD BUT CAN STILL BE OPTIMIZED
#         p1 = p2 = 0
        
#         while p2 < len(nums):
#             if nums[p2] != 0:
#                 nums[p1] = nums[p2]
#                 p1 += 1
#                 p2 += 1
#             else:
#                 p2 += 1
                
#         while p1 < len(nums):
#             nums[p1] = 0
#             p1 += 1
        