class Solution:
    def subsetsWithDup(self, nums):
        res = []
        subs = []
        nums.sort()
        
        def dfs(ind):
            if ind >= len(nums):
                res.append(subs.copy())
                return
            
            #CHOICE TO ADD
            subs.append(nums[ind])
            dfs(ind + 1)
            subs.pop()
        
            while ind + 1 < len(nums) and nums[ind] == nums[ind+ 1]:
                ind += 1
                
            dfs(ind + 1)
            
        dfs(0)
            
        return res