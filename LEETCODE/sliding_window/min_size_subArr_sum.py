class Solution:
    def minSubArrayLen(self, target, nums):
        back = front = sum_ = counter = 0
        finale = float("inf")
        
        # MY APPROACH - ACCEPTED
#         while front < len(nums) + 1:
#             if sum_ >= target:
#                 finale = min(finale, counter)
#                 sum_ -= nums[back]
#                 back += 1
#                 counter -= 1
#             else:
#                 if front < len(nums):
#                     sum_ += nums[front]
#                     counter += 1
#                 front += 1
                
#         return 0 if finale == float("inf") else finale
        
    
        # THEIRS
        
        for i in range(len(nums)):
            sum_ += nums[i]
            
            while sum_ >= target:
                counter = i + 1 - back
                finale = min(finale, counter)
                sum_ -= nums[back]
                back += 1
                
        return 0 if finale == float("inf") else finale
            
        