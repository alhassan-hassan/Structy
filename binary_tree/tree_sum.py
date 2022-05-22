def tree_sum(root):
    if not root:
        return 0
  
    left = tree_sum(root.left)
    right = tree_sum(root.right)
    return root.val + left + right
#   if not root:
#     return 0
  
#   arr = [root]
#   total = 0
  
#   while arr:
#     cur = arr.pop()
#     total += cur.val
#     if cur.right:
#       arr.append(cur.right)
#     if cur.left:
#       arr.append(cur.left)
      
#   return total