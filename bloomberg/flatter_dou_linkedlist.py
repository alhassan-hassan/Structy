
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        pseudoHead = Node(0, None, head, None)
        prev = pseudoHead
        stack = [head]

        while stack:
            cur = stack.pop()
            prev.next = cur
            cur.prev = prev
            prev = cur

            if cur.next:
                stack.append(cur.next)
            
            if cur.child:
                stack.append(cur.child)
                cur.child = None
            
            
        pseudoHead.next.prev = None

        return pseudoHead.next



        # if not head:
        #     return head

        # cur = head
        # stack = []
        # res = []

        # while cur is not None or len(stack) > 0:
        #     if cur is None:
        #         cur = stack.pop().next
        #     else:
        #         res.append(cur.val)
        #         if cur.child:
        #             stack.append(cur)
        #             cur = cur.child
        #         else:
        #             cur = cur.next

        # return Node(",".join(str(x) for x in res))



        
        if not head:
            return None
        
        stack = []
        res = []
        
        cur = head
        
        while cur is not None or len(stack) > 0:
            
            if cur is None:
                cur = stack.pop().next
            else:
                res.append(cur.val)
                if cur.child is not None:
                    stack.append(cur)
                    cur = cur.child
                else:
                    cur = cur.next
                    
        return Node(",".join(str(x) for x in res))
        