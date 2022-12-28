from collections import deque
def closest_carrot(grid, starting_row, starting_col):
  dq = deque([(starting_row, starting_col, 0)])
  visited = set([starting_row, starting_col])
  
  while dq:
    row, col, count = dq.popleft()
    if grid[row][col] == "C":
      return count
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for d_row, d_col in moves:
      row_neighbor = row + d_row
      col_neighbor = col + d_col
      
      r_inbound = 0<=row_neighbor < len(grid)
      c_inbound = 0<=col_neighbor < len(grid[0])
      
      pos = (row_neighbor, col_neighbor)
      
      if r_inbound and c_inbound and pos not in visited and grid[row_neighbor][col_neighbor] != "X":
        visited.add(pos)
        dq.append((row_neighbor, col_neighbor, count + 1))
    
  return -1