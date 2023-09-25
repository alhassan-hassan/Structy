# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # BETTER APPROACH: Linear and constant for time and space respectively
        cur = head
        while cur.next:
            if cur.val > cur.next.val:
                tempt = cur.next
                cur.next = tempt.next
                tempt.next = head
                head = tempt
            else:
                cur = cur.next

        return head


        # HIGHER COMPLEXITY. NlogN for time and linear for space
        if not head or not head.next:
            return head

        # Create an array to store the values from the linked list
        values = []
        cur = head

        while cur:
            values.append(cur.val)
            cur = cur.next

        # Sort the values
        values.sort()

        # Reconstruct the sorted linked list
        dummy = ListNode(0)
        cur = dummy

        for val in values:
            cur.next = ListNode(val)
            cur = cur.next

        return dummy.next
