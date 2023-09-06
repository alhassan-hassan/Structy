# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    # OPTION 1
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def summer(node):
            sum_ = 0
            cur = node

            while cur:
                sum_ = sum_ * 10 + cur.val
                cur = cur.next
            return sum_

        num1 = summer(l1)
        num2 = summer(l2)

        total = num1 + num2

        dummy = ListNode(0)
        cur = dummy

        for num in str(total):
            cur.next = ListNode(num)
            cur = cur.next

        return dummy.next


        # OPTION 2
        
        def getNumbers(node):
            nums = []
            cur = node

            while cur:
                nums.append(cur.val)
                cur = cur.next

            return nums

        list1 = getNumbers(l1)
        list2 = getNumbers(l2)

        carry = 0
        head = None

        while list1 or list2 or carry != 0:
            sum_ = carry
            if list1: sum_ += list1.pop()
            if list2: sum_ += list2.pop()

            newNode = ListNode(sum_ % 10)
            newNode.next = head
            head = newNode

            carry = sum_ // 10

        return head
    
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def nums(head):     
            cur = head
            res = []

            while cur:
                res.append(cur.val)
                cur = cur.next

            return res

        stack1 = nums(l1)
        stack2 = nums(l2)

        carry = 0
        head = None

        while stack1 or stack2 or carry != 0:
            sum_ = carry

            if stack1:
                sum_ += stack1.pop()
            
            if stack2:
                sum_ += stack2.pop()

            newNode = ListNode(sum_ % 10)
            newNode.next = head
            head = newNode

            carry = sum_ // 10

        return head
        # def getNumbers(node):
        #     nums = []
        #     cur = node

        #     while cur:
        #         nums.append(cur.val)
        #         cur = cur.next

        #     return nums

        # list1 = getNumbers(l1)
        # list2 = getNumbers(l2)

        # carry = 0
        # head = None

        # while list1 or list2 or carry != 0:
        #     sum_ = carry
        #     if list1: sum_ += list1.pop()
        #     if list2: sum_ += list2.pop()

        #     newNode = ListNode(sum_ % 10)
        #     newNode.next = head
        #     head = newNode

        #     carry = sum_ // 10

        # return head
            
            


        
        



