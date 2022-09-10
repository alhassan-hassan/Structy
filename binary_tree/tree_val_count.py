def val_count(root, target):
    if not root: return 0

    left = val_count(root.left, target)
    right = val_count(root.right, target)

    if root.val == target:
        return 1 + left + right
    return left + right