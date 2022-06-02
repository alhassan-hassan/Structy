class Solution:
    def triangularSum(self, nums) -> int:
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return nums[0]
        
        arr = nums
        
        for i in range(len(nums) - 1):
            tempt = arr
            moment = []
            
            for j in range(1, len(tempt)):
                moment.append((tempt[j-1] + tempt[j]) % 10)
                
            arr = moment
            
        return arr[0]
        