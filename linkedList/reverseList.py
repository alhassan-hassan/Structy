# Iterative apprach MINE
def reverse_list(head):
  prev=None
  current=head
  while current is not None:
    next=current.next
    current.next=prev
    prev=current
    current=next
    
  return prev

# ITERATIVELY
def reverse_list(head, prev = None):
  if head is None:
    return prev
  next = head.next
  head.next = prev
  return reverse_list(next, head)

  