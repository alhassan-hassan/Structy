# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # o(n^2) for the hashing in the hashmap and finding subtrees.
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = defaultdict(int)

        def dfs(node):
            if not node:
                return "null"

            subtree = ",".join([str(node.val), dfs(node.left), dfs(node.right)])

            if subtrees[subtree] == 1:
                res.append(node)
            subtrees[subtree] += 1

            return subtree


        res = []
        dfs(root)
        return res


# BETTER APPROACH
    def findDuplicateSubtrees(self, root):
        def traverse(node):
            if not node:
                return 0
            triplet = (traverse(node.left), node.val, traverse(node.right))
            if triplet not in triplet_to_id:
                triplet_to_id[triplet] = len(triplet_to_id) + 1
            id = triplet_to_id[triplet]
            cnt[id] += 1
            if cnt[id] == 2:
                res.append(node)
            return id
        triplet_to_id = dict()
        cnt = collections.defaultdict(int)
        res = []
        traverse(root)
        return res
        