class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counts = [0] * 26

        for i in range(len(s)):
            counts[ord(s[i]) - 97] += 1
            counts[ord(t[i]) - 97] -= 1

        return sum([x if x > 0 else 0 for x in counts])
    

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        memo1 = defaultdict(int)

        for char in s:
            memo1[char] += 1

        count = 0
        for char in t:
            if char in memo1 and memo1[char]:
                memo1[char] -= 1

        return sum(memo1.values())


"""
COMPLEXITIES: TIME : O(max(n, m))
              SPACE: O(m)
"""