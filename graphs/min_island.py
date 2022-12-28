def minimum_island(grid):
  visited = set()
  minimum = float("inf")
  
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      size = explore(grid, r, c, visited)
      if size > 0:
        minimum = min(size, minimum)
              
  return minimum


def explore(grid, r, c, visited):
  r_inbounds = 0 <= r < len(grid)  
  c_inbounds = 0 <= c < len(grid[0])
  
  if not r_inbounds or not c_inbounds:
    return 0
  
  if grid[r][c] == "W":
    return 0
  
  pos = (r, c)
  if pos in visited:
    return 0
  
  visited.add(pos)
  
  size = 1
  size += explore(grid, r - 1, c, visited)
  size += explore(grid, r + 1, c, visited)
  size += explore(grid, r, c - 1, visited)
  size += explore(grid, r, c + 1, visited)
  
  return size