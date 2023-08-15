import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def explore_adjacebt_islands(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r,c))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while q:
                row, col = q.popleft()

                for rd, cd in directions:
                    cr = row + rd
                    cc = col + cd

                    if (cr in range(rows) and 
                        cc in range(cols) and 
                        grid[cr][cc] == "1" and 
                        (cr, cc) not in visited):

                        q.append((cr, cc))
                        visited.add((cr, cc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    explore_adjacebt_islands(r, c)
                    islands += 1

        return islands
    

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