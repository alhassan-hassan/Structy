# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # def validate(node, low = -math.inf, high = math.inf):
        #     if not node:
        #         return True

        #     if node.val <= low or node.val >= high:
        #         return False

        #     return (validate(node.right, node.val, high) and validate(node.left, low, node.val))

        # return validate(root)

        stack = [(root, -math.inf, math.inf)]

        while stack:
            node, lower, higher = stack.pop()

            if node.val <= lower or node.val >= higher:
                return False

            if node.left:
                stack.append((node.left, lower, node.val))

            if node.right:
                stack.append((node.right, node.val, higher))

        return True            
    



def getMaxAlternatingMusic(music: str, k: int) -> int:
    def max_alternating(music: str, k: int, pattern_start: str) -> int:
        n = len(music)
        left = 0  # Left pointer of the sliding window
        flips = 0  # Number of flips needed in the current window
        max_len = 0  # Maximum length of alternating substring

        for right in range(n):
            # Determine the expected character in the alternating pattern
            expected_char = pattern_start if (right % 2 == 0) else ('1' if pattern_start == '0' else '0')
            
            # If the current character does not match the expected character, we need a flip
            if music[right] != expected_char:
                flips += 1

            # If flips exceed k, shrink the window from the left
            while flips > k:
                expected_left_char = pattern_start if (left % 2 == 0) else ('1' if pattern_start == '0' else '0')
                if music[left] != expected_left_char:
                    flips -= 1
                left += 1

            # Update the maximum length of the alternating substring found so far
            max_len = max(max_len, right - left + 1)

        return max_len

    # Try both patterns: starting with '0' and starting with '1'
    return max(max_alternating(music, k, '0'), max_alternating(music, k, '1'))

# Example usage:
music = "1001"
k = 1
print(getMaxAlternatingMusic(music, k))  # Output: 3
