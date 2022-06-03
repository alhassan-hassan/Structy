# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def findTarget(self, root, k):
        if not root:
            return False
        
        dic = {}
        dq = deque([root])
        
        while len(dq) > 0:
            cur = dq.popleft()
            if k - cur.val in dic:
                return True
            
            dic[cur.val] = "T"

            if cur.left:
                dq.append(cur.left)
            if cur.right:
                dq.append(cur.right)
                
        return False
        