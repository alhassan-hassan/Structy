class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(cur, i):
            if i >= len(nums):
                ans.append(cur[:])
                return
            
            # DESICION TO INCLUSE NUMS[I]
            cur.append(nums[i])
            dfs(cur, i + 1)

            # DECISION NOT TO INCLUDE NUMS[I]
            cur.pop()
            dfs(cur, i + 1)

        ans = []
        dfs([], 0)

        return ans

# TIME : O(n * 2 ^ n)