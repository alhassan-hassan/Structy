class Solution:
    def removeDuplicates(self, nums) -> int:
        
        # THEIR APPROACH
#         if len(nums) == 0:
#             return 0
        
#         track = 0
        
#         for i in range(1, len(nums)):
#             if nums[track] != nums[i]:
#                 track += 1
#                 nums[track] = nums[i]
                
#         return track + 1
    
    # MY APPROACH - BEST
    
        sl = 0
        fs = 1
        track = 1

        if len(nums) <= 1:
            return len(nums)

        while fs < len(nums):
            if nums[sl] == nums[fs]:
                fs += 1
            else:
                nums[track] = nums[fs]
                track += 1
                sl = fs
                fs += 1
                
        return track

    
    
    
    
    
    
    
    
    
    
    
        
#         if len(nums) == 0:
#             return []
        
#         ind = 0
#         slow = 0
#         fast = 0
        
#         while fast < len(nums):
#             if fast == 0:
#                 nums[ind] = nums[slow]
#                 ind += 1
#                 fast += 1
#             else:
#                 if nums[slow] == nums[fast]:
#                     fast += 1
#                 else:
#                     nums[ind] = nums[fast]
#                     slow = fast
#                     fast += 1
#                     ind += 1
                    
#         nums[ : ] = nums[ 0 : ind]
                    
            
        
        