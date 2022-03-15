class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

# The lInkedList generated

a.next = b
b.next = c
c.next = d

# Recursive traversal

def traverse(head):
    if head is None:
        return
    print(head.val)
    traverse(head.next)

traverse(a)

# LinkedList Values
def linked_list_values(head):
  values = []
  _linked_list_values(head, values)
  return values

def _linked_list_values(head, values):
  if head is None:
    return
  values.append(head.val)
  _linked_list_values(head.next, values)