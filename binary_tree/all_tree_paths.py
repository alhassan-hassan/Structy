

def all_tree_paths(root):
  if not root:
    return []
  
  if not root.left and not root.right:
    return [[root.val]]
  
  paths = []
  
  left = all_tree_paths(root.left)
  for path in left:
    paths.append([root.val, *path])
    
  right = all_tree_paths(root.right)
  for path in right:
    paths.append([root.val, *path])
    
  return paths
  