class Solution:
    def maxDepth(self, s: str) -> int:
        open_, depth = 0, 0

        for char in s:
            if char == "(":
                open_ += 1
            if char == ")":
                open_ -= 1

            depth = max(depth, open_)

        return depth