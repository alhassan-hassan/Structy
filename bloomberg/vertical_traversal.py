# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        dic = collections.defaultdict(list)
        dq = collections.deque([(root, 0)])

        dq = deque([(root, 0)])

        min_index = max_index = 0

        while dq:
            node, index = dq.popleft()

            if node is not None:
                dic[index].append(node.val)

                dq.append((node.left, index - 1))
                dq.append((node.right, index + 1))

                min_index = min(min_index, index)
                max_index = max(max_index, index)

        return [dic[index] for index in range(min_index, max_index + 1)]


    