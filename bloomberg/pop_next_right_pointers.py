"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        dq = collections.deque([root])

        while dq:
            size = len(dq)
            for i in range(size):
                node = dq.popleft()
                if i < size - 1 :
                    node.next = dq[0]
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return root






