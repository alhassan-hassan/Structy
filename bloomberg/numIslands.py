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

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        islands = 0

        def bfs(r, c):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            dq = deque([(r,c)])

            while dq:
                rr, cc = dq.popleft()
                for rd, cd in directions:
                    nr = rr + rd
                    nc = cc + cd

                    if nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in seen and grid[nr][nc] == "1":
                        seen.add((nr,nc))
                        dq.append((nr,nc))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in seen:
                    bfs(i, j)
                    islands += 1

        return islands





















        # if not grid:
        #     return 0

        # def dfs(x, y):
        #     # Base case: return if we are out of bounds or at a water cell
        #     if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '0':
        #         return
        #     # Mark the current cell as visited by setting it to '0'
        #     grid[x][y] = '0'
        #     # Explore all four directions
        #     dfs(x + 1, y)  # Down
        #     dfs(x - 1, y)  # Up
        #     dfs(x, y + 1)  # Right
        #     dfs(x, y - 1)  # Left

        # island_count = 0

        # # Traverse the entire grid
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == '1':  # Start of a new island
        #             island_count += 1  # Increment island count
        #             dfs(i, j)  # Mark the entire island as visited

        # return island_count
        # if not grid:
        #     return 0

        # rows, cols = len(grid), len(grid[0])
        # visited = set()
        # islands = 0

        # def bfs(r, c):
        #     queue = deque([(r, c)])
        #     directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        #     while queue:
        #         rr, cc = queue.popleft()
        #         for rd, cd in directions:
        #             r, c = rr + rd, cc + cd

        #             if r in range (rows) and c in range(cols) and (r, c) not in visited and grid[r][c] == "1":
        #                 queue.append((r, c))
        #                 visited.add((r, c))
                
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r, c) not in visited:
        #             bfs(r, c)
        #             islands += 1

        # return islands


"""
COMPLEXITIES: TIME : O(N * M)
              SPACE: -------
"""
