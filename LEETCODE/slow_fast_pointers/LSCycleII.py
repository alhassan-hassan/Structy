# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        # HARE AND TOITOISE 0(1) SPACE
        def intersection(head):
            tort = head
            hare = head

            while hare and hare.next:
                hare = hare.next.next
                tort = tort.next
                if tort == hare:
                    return tort
            return None
        
        def theCycle(intNode):
            inter = intersection(intNode)
            
            if inter is None:
                return None
            
            cur = head
            while cur != inter:
                cur = cur.next
                inter = inter.next
                
            return cur
        
        return theCycle(head)
            
            
            
        # OPERATING IN 0(N) TIME AND COMPLEXITY
#         slow = head
#         seen = set()
        
#         while slow:
#             if slow not in seen:
#                 seen.add(slow)
#                 slow = slow.next
#             else:
#                 return slow
#         return None