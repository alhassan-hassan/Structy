from collections import deque


def brv(root):
    if not root : return None

    dq = deque([root])
    cur = None
    
    while dq:
        cur = dq.popleft()

        if cur.left:
            dq.append(cur.left)

        if cur.right:
            dq.append(cur.right)

    return cur.val
