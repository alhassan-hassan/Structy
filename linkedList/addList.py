class Node:
      def __init__(self, val):
    self.val = val
    self.next = None

def add_lists(head_1, head_2):
  num1 = ""
  num2 = ""
  
  cur1 = head_1
  cur2 = head_2
  
  while cur1:
    num1 += str(cur1.val)
    cur1 = cur1.next
    
  while cur2:
    num2 += str(cur2.val)
    cur2 = cur2.next
    
  total = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
  
  dummy = Node(None)
  tail = dummy
  
  for num in total:
    tail.next = Node(num)
    tail = tail.next
    
  return dummy.next