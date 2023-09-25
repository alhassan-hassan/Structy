class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True

        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append([s1[i], s2[i]])

        if len(diff) == 2 and diff[0] == diff[-1][::-1]:
            return True
        return False
        """
        s1 = "bank", s2 = "kanb"
        diff = [[b, k], [k, b]]

        diff[0] = [b, k]
        diff[-1][::-1] = [b, k]


        Time complexity:O(N)
        Space complexity:O(1)
        """

        