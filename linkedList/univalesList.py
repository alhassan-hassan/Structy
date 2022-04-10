class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def is_univalue_list(head):
  val = head.val
  cur = head.next  
  while cur is not None:
    if cur.val != val:
      return False
    cur = cur.next
    
  return True