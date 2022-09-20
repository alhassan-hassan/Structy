def leaf_list(root):
  
  if not root:
    return []
  
  if root.left is None and root.right is None:
    return [root.val]
  
  left=leaf_list(root.left)
  right=leaf_list(root.right)
  
  return [*left,*right]