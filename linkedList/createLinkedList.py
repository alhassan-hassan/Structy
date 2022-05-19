class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None
    
def create_linked_list(list):
  dummy = Node()
  tail = dummy
  
  for val in list:
    tail.next = Node(val = val)
    tail = tail.next
    
  return dummy.next
  