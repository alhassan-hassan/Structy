class Solution:
    def threeSumClosest(self, nums, target):
        """
            [-1, 2 , 1 , -4]   [-4, -1, 1, 2]     1
                                 *
                                     *     *
                                     
                                     sum1 = -3 diff = 4
                                     sum2 = -1 diff = 2
                                     
                                     sum3 = 
                                     
                              
            
            [-100, -98, -2, -1]    -101
               *
                    *         *
        """
        
        nums = sorted(nums)
        closest = float("inf")
        diff = float("inf")
        
        for i in range(len(nums)):
            p1 = i + 1
            p2 = len(nums) - 1
            
            while p1 < p2:
                summ = nums[i] + nums[p1] + nums[p2]
                difference = target - summ
                
                if abs(difference) < abs(diff):
                    diff = difference
                    closest = summ
                    
                if summ < target:
                    p1 += 1
                else :
                    p2 -= 1
            if diff == 0:
                break
                        
        return closest
                    
                
    
    
    
    
    