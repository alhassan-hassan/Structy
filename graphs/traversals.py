graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

def dfs(graph, start):
    stack = [start]
    
    while stack:
        cur = stack.pop()
        print(cur)
        for neighbor in graph[cur]:
            stack.append(neighbor)
        
dfs(graph, "a")