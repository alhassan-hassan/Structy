graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}

def largest_component(graph):
  visited = set()
  largest = 0
  
  for node in graph:
    size = component_size(graph, node, visited)
    largest = max(largest, size)
    
  print(largest)

def component_size(graph, current, visited):
  if current in visited:
    return 0
  visited.add(current)
  
  size = 1
  
  for neighbor in graph[current]:
    size += component_size(graph, neighbor, visited)
    
  return size

largest_component(graph)