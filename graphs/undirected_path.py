from collections import *
# BFS
def undirected_path(edges, node_A, node_B):
  dq = deque([node_A])
  
  while dq:
    cur = dq.popleft()
    
    if cur == node_B:
      return True
    
    for node in edges[cur]:
      dq.append(node)
      
  return False

  # DFS
  '''
  Time com=o(e)
  Space com=o(n)
'''
import collections
def undirected_path(edges, node_A, node_B):
  graph = build_graph(edges)
  return has_path(graph, node_A, node_B, set())

def has_path(graph, src, dst, visited):
  if src == dst:
    return True
  if src in visited:
    return False
  visited.add(src)
  
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst, visited) == True:
      return True
    
  return False


def build_graph(edges):
  graph = collections.defaultdict(list)
  for a,b in edges:
    graph[a].append(b)    
    graph[b].append(a)
    
  return graph