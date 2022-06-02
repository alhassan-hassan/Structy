import math
def tree_min_value(root):
  if not root:
    return float("-inf")
  min_ = root.val
  arr = [root]
  
  while arr:
    cur = arr.pop()
    if cur.val < min_:
      min_ = cur.val
      
    if cur.right:
      arr.append(cur.right)
      
    if cur.left:
      arr.append(cur.left)
      
  return min_
  
  
#   if not root:
#     return math.inf
#   left=tree_min_value(root.left)
#   right=tree_min_value(root.right)
  
#   return min(root.val,left,right)