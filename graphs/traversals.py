from collections import deque
graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

# 1. DFS
# ITERATIVELY
def dfs(graph, start):
    stack = [start]
    
    while stack:
        cur = stack.pop()
        print(cur)
        for neighbor in graph[cur]:
            stack.append(neighbor)
        
# dfs(graph, "a")

# RECURSIVELY
def dfs_recur(graph, start):
    print(start)
    for neighbor in graph[start]:
        dfs_recur(graph, neighbor)
        
# dfs_recur(graph, "a")


# 2. BFS
def bfs(graph, current):
    dq = deque([current])
    while dq:
        cur = dq.popleft()
        print(cur)
        for neighbor in graph[cur]:
            dq.append(neighbor)
            
bfs(graph, "a")
    