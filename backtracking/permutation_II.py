class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(cur):
            if len(cur) == len(nums):
                ans.append(cur[:])

            for num in numHash:
                if numHash[num] > 0:
                   numHash[num] -= 1
                   cur.append(num)
                   dfs(cur)
                   numHash[num] += 1
                   cur.pop()

        ans = []
        numHash = Counter(nums)
        dfs([])

        return ans