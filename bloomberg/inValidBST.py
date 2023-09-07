# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # def dfs(node, low, high):
        #     if not node:
        #         return True

        #     if node.val <= low or node.val >= high:
        #         return False

        #     return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
            

        # return dfs(root, -math.inf, math.inf)
            
        stack = [(root, -math.inf, math.inf)]

        while stack:
            node, low, high = stack.pop()
            if node:
                if node.val <= low or node.val >= high:
                    return False

                stack.append((node.left, low, node.val))
                stack.append((node.right, node.val, high))

        return True
        