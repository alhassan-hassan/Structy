# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        # RECURSIVELY
#         if not root:
#             return False
        
#         targetSum -= root.val
#         if not root.left and not root.right:
#             return targetSum == 0
        
#         return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    
        
        # ITERATIVELY
        if not root:
            return False
        
        dq = [(root, targetSum - root.val)]
        while dq:
            node, target = dq.pop()
            if not node.left and not node.right and target == 0:
                return True
            if node.right:
                dq.append((node.right, target - node.right.val))
            
            if node.left:
                dq.append((node.left, target - node.left.val))
                
        return False