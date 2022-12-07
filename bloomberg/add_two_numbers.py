# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def list_to_stack(head):
            stack = []
            while head:
                stack.append(head.val)
                head = head.next
            return stack

        stack1 = list_to_stack(l1)
        stack2 = list_to_stack(l2)

        head = None

        carry = 0
        while stack1 or stack2 or carry != 0:
            sum_ = carry
            if stack1: sum_ += stack1.pop()
            if stack2: sum_ += stack2.pop()

            newNode = ListNode(sum_ % 10)
            newNode.next = head
            head = newNode

            carry = sum_ // 10

        return head



