class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def remove_node(head, target_val):
  if head.val==target_val:
    return head.next
  # a -> b -> c -> d -> e -> f
  
  current=head
  while current is not None: 
    value=current.next.val
    if value==target_val:
      current.next=current.next.next
      return head
    
    current=current.next

def insert_node(head, value, index):
    node=Node(value)
    track=1
    current=head
    if index==0:
        node.next=head
        return node
    
    
    while current is not None:
        # print("I am here")
        if index==track:
            current_next=current.next
            current.next=node
            node.next=current_next
        
        track+=1
        current=current.next
    return head
  