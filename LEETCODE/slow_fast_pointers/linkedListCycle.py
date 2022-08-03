# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) :
        
        # USING POINTERS
        if not head:
            return False
        slow = head
        fast = head.next
        
        while fast and fast.next:
            if slow != fast:
                slow = slow.next
                fast = fast.next.next
            else:
                return True
        return False
    
        # USING A HASHMAP
        # if not head:
        #     return False
        # dic = set()
        # cur = head
        # while cur.next:
        #     if cur in dic:
        #         return True
        #     dic.add(cur)
        #     cur = cur.next
        # return False
            
        
            
        