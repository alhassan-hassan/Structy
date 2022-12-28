import collections
# USING DFS COULD LEAD TO EXPLORING USELESS PATHS THAT SENDS US AWAY
# FROM EVEN THE TARGET NODE

# HENCE BFS WOULD BE MORE USEFUL AND EFFICIENT HERE
def shortest_path(edges, node_A, node_B):
  graph = makeGraph(edges)
  visited = set([node_A])
  
  dq = collections.deque([(node_A, 0)])
  
  while dq:
    node,count = dq.popleft()
    if node == node_B:
      return count
    
    visited.add(node)
    
    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        dq.append((neighbor, count + 1))
      
  return -1
  

def makeGraph(edges):
  graph = collections.defaultdict(list)

  for s,e in edges:
    graph[s].append(e)
    graph[e].append(s)

  return graph
  
  
  