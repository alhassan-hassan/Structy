def tree_includes(root, target):
    #   if not root:
#     return False
  
#   if root.val == target:
#     return True
  
#   left = tree_includes(root.left, target)
#   right = tree_includes(root.right, target)
  
#   return left or right


  # ITERATIVELY
  if not root:
    return False
  
  arr =[root]
  while arr:
    cur = arr.pop()
    if cur.val == target:
      return True
    if cur.left:
      arr.append(cur.left)
    if cur.right:
      arr.append(cur.right)
      
  return False