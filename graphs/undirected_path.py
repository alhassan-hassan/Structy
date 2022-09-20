from collections import *
def undirected_path(edges, node_A, node_B):
  dq = deque([node_A])
  
  while dq:
    cur = dq.popleft()
    
    if cur == node_B:
      return True
    
    for node in edges[cur]:
      dq.append(node)
      
  return False