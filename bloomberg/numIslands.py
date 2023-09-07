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
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while queue:
                rr, cc = queue.popleft()
                for rd, cd in directions:
                    r, c = rr + rd, cc + cd

                    if r in range (rows) and c in range(cols) and (r, c) not in visited and grid[r][c] == "1":
                        queue.append((r, c))
                        visited.add((r, c))
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands


"""
COMPLEXITIES: TIME : O(N * M)
              SPACE: -------
"""
