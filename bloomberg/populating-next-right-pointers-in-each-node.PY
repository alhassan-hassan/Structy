"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # BETTER APPROACH - linear for time and constant for space
        if not root:
            return root

        leftmost = root
        while leftmost.left:
            head = leftmost

            while head:
                head.left.next = head.right

                if head.next:
                    head.right.next = head.next.left

                head = head.next

            leftmost = leftmost.left

        return root

        # if not root:
        #     return root

        # dq = deque([root])

        # while dq:
        #     size = len(dq)

        #     for i in range(size):
        #         node = dq.popleft()

        #         if i < size - 1:
        #             node.next = dq[0]

        #         if node.left:
        #             dq.append(node.left)
        #         if node.right:
        #             dq.append(node.right)

        # return root
    # LINEAR FOR BOTH COMPLEXITIES


    # FROM LEETCODE

        
        if not root:
            return root
        
        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root
        
        # Once we reach the final level, we are done
        while leftmost.left:
            
            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the 
            # corresponding links for the next level
            head = leftmost
            while head:
                
                # CONNECTION 1
                head.left.next = head.right
                
                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left
                
                # Progress along the list (nodes on the current level)
                head = head.next
            
            # Move onto the next level
            leftmost = leftmost.left
        
        return root 

        