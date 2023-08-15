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
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        verts = defaultdict(list)
        queue = deque([(root, 0)])

        min_ = max_ = 0

        while queue:
            node, ind = queue.popleft()
            if node is not None:
                verts[ind].append(node.val)

                queue.append((node.left, ind - 1))
                queue.append((node.right, ind + 1))

                min_ = min(min_, ind)
                max_ = max(max_, ind)

        output = []

        for key in range(min_, max_ + 1):
            output.append(verts[key])

        return output

"""
COMPLEXITIES: TIME: O(N)
              SPACE:O(N)
"""


    