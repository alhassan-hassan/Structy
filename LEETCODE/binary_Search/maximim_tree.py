# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        [3,2,1,6,0,5]
        
        
        def helper(arr, start, end):
            start and end within the contraint of 0 and the length of the current array
            
            max = max(arr)    ind = max
            
            node = Treenode(arr[max])
            node.left = helper(arr, start, ind)
            node.right = helper(arr, ind + 1, end)
            
            return node
        """
        if len(nums) == 0: return None
        return self.helper(nums, 0, len(nums) - 1)
        
    def helper(self, arr, start, end):
        if start < 0 or end >= len(arr) or start > end:
            return None

        head = max(arr[start : end + 1])
        ind = arr.index(head)
        node = TreeNode(head)
        node.left = self.helper(arr, start, ind-1)
        node.right = self.helper(arr, ind + 1, end)

        return node
            
        
            
            
            