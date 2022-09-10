def pathfinder(root, target):
    res = finder(root, target)
    return None if res is None else res


def finder(root, target):
    if not root: return None

    if root.val == target:
        return [root.val]

    left = finder(root.left, target)
    if left is not None:
        left.append(root.val)
        return left

    right = finder(root.right, target)
    if right is not None:
        right.append(root.val)
        return right

    return None
