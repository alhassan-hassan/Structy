
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head):
        if not head:
            return None
        
        stack = []
        res = []
        
        cur = head
        
        while cur is not None or len(stack) > 0:
            
            if cur is None:
                cur = stack.pop().next
            
            if cur is not None:
                res.append(cur.val)
                if cur.child is not None:
                    stack.append(cur)
                    cur = cur.child
                else:
                    cur = cur.next
                    
        return Node(",".join(str(x) for x in res))
        