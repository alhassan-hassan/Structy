class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummyNode = ListNode(0)
        cur = dummyNode
        
        while l1 or l2 or carry != 0:
            sum_ = carry
            sum_ += l1.val if l1 else 0
            sum_ += l2.val if l2 else 0

            newNode = ListNode(sum_ % 10)
            cur.next = newNode
            cur = newNode

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            carry = sum_ // 10
        
        return dummyNode.next

        