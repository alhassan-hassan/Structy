class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        charSet = set()
        l = 0
        count = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            count = max(count, r - l + 1)

        return count


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = set()
        count = lo = 0

        for r in range(len(s)):
            while s[r] in track:
                track.remove(s[lo])
                lo += 1

            track.add(s[r])

            count = max(count, r - lo + 1)

        return count

"BOTH TIME AND SPACE IS O(N)"
