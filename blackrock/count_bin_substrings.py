class Solution(object):
    def countBinarySubstrings(self, s):

        ans, prev, cur = 0, 0, 1

        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        ans += min(prev, cur)

        return ans 

        # track = 1
        # groups = []

        # for i in range(1, len(s)):
        #     if s[i-1] != s[i]:
        #         groups.append(track)
        #         track = 1
        #     else:
        #         track += 1
        # groups.append(track)
        

        # ans = 0
        # for i in range(1, len(groups)):
        #     ans += min(groups[i-1], groups[i])
        # return ans