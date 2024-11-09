class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        mem = {}
        arr.sort()

        for i, x in enumerate(arr):
            mem[x] = 1
            for j in range(i):
                y = arr[j]
                if x % y == 0:
                    z = x // y
                    if z in mem:
                        mem[x] += mem[y] * mem[z]
                        mem[x] %= MOD
        
        return sum(mem.values()) % MOD














        # def dfs(x):
        #     if x in mem:
        #         return mem[x]
            
        #     mem[x] = 1

        #     for y in arr:
        #         if y > x:
        #             break
        #         if x % y == 0:
        #             z = x // y
        #             if z in mem:
        #                 mem[x] += mem[y] * mem[z]
        #                 mem[x] %= MOD
            
        #     return mem[x]

        # total_trees = sum(dfs(x) for x in arr) % MOD
        # return total_trees


"""
	Complexity:
	•	Time Complexity: This approach is  O(n^2) , where  n  is the length of arr. Each number requires checking factors within the array, and memoization optimizes repeated subproblems.
	•	Space Complexity:  O(n) , for storing dp.
"""


















        # arr.sort()  # Step 1: Sort arr
        # dp = {}  # Initialize dictionary for dynamic programming

        # # Step 2: Count ways for each element
        # for i, x in enumerate(arr):
        #     print(i)
        #     dp[x] = 1  # Every number itself can be a single-node tree
        #     for j in range(i):  # Check all elements before x
        #         y = arr[j]
        #         if x % y == 0:  # y must be a factor
        #             z = x // y  # The other factor
        #             if z in dp:  # Check if z is in the array
        #                 dp[x] += dp[y] * dp[z]
        #                 dp[x] %= MOD  # Keep it within mod limit

        # # Step 3: Return sum of all ways for each element in arr
        # return sum(dp.values()) % MOD

"""
	Complexity:
	•	Time Complexity: This approach is  O(n^2) , where  n  is the length of arr. Each number requires checking factors within the array, and memoization optimizes repeated subproblems.
	•	Space Complexity:  O(n) , for storing dp.
"""

        # arr.sort()  # Step 1: Sort arr
        # dp = {}  # Initialize dictionary for dynamic programming

        # # Step 2: Count ways for each element
        # for i, x in enumerate(arr):
        #     print(i)
        #     dp[x] = 1  # Every number itself can be a single-node tree
        #     for j in range(i):  # Check all elements before x
        #         y = arr[j]
        #         if x % y == 0:  # y must be a factor
        #             z = x // y  # The other factor
        #             if z in dp:  # Check if z is in the array
        #                 dp[x] += dp[y] * dp[z]
        #                 dp[x] %= MOD  # Keep it within mod limit

        # # Step 3: Return sum of all ways for each element in arr
        # return sum(dp.values()) % MOD