def connected_components_count(graph):
  visited = set()
  count = 0
  
  for node in graph:
    if explore(graph, node, visited) == True:
      count += 1
      
  return count
  
def explore(graph, current, visited):
  if current in visited:
    return False
  visited.add(current)
  
  for neigbor in graph[current]:
    explore(graph, neigbor, visited)
    
  return True
    
  
  