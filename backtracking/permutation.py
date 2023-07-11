class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # def backtrack(cur):
        #     if len(cur) == len(nums):
        #         ans.append(cur[:])
        #         return

        #     for num in nums:
        #         if num not in cur:
        #             cur.append(num)
        #             backtrack(cur)
        #             cur.pop()

        # ans = []
        # backtrack([])

        # return ans

        def dfs(cur, used):
            if len(cur) == len(nums):
                ans.append(cur[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    cur.append(nums[i])
                    dfs(cur, used)
                    cur.pop()
                    used[i] = False

        ans = []
        used = [False] * len(nums)
        dfs([], used)

        return ans