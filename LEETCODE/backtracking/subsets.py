class Solution:
    def subsets(self, nums):
        res = []
        sub = []
        def subsets(ind):
            if ind >= len(nums):
                res.append(sub.copy())
                return
            
            sub.append(nums[ind])
            subsets(ind + 1)
            
            sub.pop()
            subsets(ind + 1)
            
        subsets(0)
        
        return res
        