class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1): #0(N)
            for word in wordDict:  #O(M)
                if (i + len(word) <= len(s) and s[i : i + len(word)] == word): #(O(N))
                    dp[i] = dp[i + len(word)]

                if dp[i]:
                    break

        return dp[0]

    """
     COMPLEXITIES: TIME : O(N^2(s) * M(word dict))
                   SPACE: O(N)
    """