# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        
        if not head:
            return False
        
        slow = fast = head
        
        while fast:
            slow = slow.next
            fast = fast.next.next
            
        return slow