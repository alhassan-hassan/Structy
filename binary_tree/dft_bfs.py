def depth_first_values(root):
    if not root:
        return []
  
    stack = [root]
    values = []
  
    while stack:
        node = stack.pop()
        values.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return values
# n = number of nodes
# Time: O(n)
# Space: O(n)

#RECURSIVE
def depth_first_values(root):
  if not root:
    return []
  
  left_values = depth_first_values(root.left)
  right_values = depth_first_values(root.right)
  return [ root.val, *left_values, *right_values ]

from collections import deque

def breadth_first_values(root):
  if not root:
    return []
  
  queue = deque([ root ])
  values = []
  
  while queue:
    node = queue.popleft()
    
    values.append(node.val)
    
    if node.left:
      queue.append(node.left)
      
    if node.right:
      queue.append(node.right)
      
  return values