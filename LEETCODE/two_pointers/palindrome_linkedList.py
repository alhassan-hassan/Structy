# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head):
        
        # REVERSE SECOND HALF IN-PLACE 
        """
            Find the end of the first half.
            Reverse the second half.
            Determine whether or not there is a palindrome.
            Restore the list.
            Return the result.
        """
        
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.second_half(head)
        second_half_start = self.reverse(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse(second_half_start)
        return result    
        
    def second_half(self,head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self,head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
            
        
        
        # OKAY BUT NOT OPTIMAL
#         cur = head
#         arr = []
#         while cur:
#             arr.append(cur.val)
#             cur = cur.next
        
#         return arr == arr[::-1]
        