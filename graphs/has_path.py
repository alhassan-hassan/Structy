from collections import deque
def has_path(graph, src, dst):
  
  # ITERATIVE;Y
#   if src == dst:
#     return True
  
#   dq = deque([src])
  
#   while dq:
#     cur = dq.popleft()
#     if cur == dst:
#       return True
    
#     for neighbor in graph[cur]:
#       dq.append(neighbor)
      
#   return False

  # RECURSIVELY
  if src == dst:
    return True
  
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst) == True:
      return True
  
  return False