class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counts = [0] * 26

        for i in range(len(s)):
            counts[ord(s[i]) - 97] += 1
            counts[ord(t[i]) - 97] -= 1

        return sum([x if x > 0 else 0 for x in counts])