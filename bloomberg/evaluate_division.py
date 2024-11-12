import collections
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        N = len(equations)

        for i in range(N):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1 / values[i]

        def dfs(x, y, visited):
            if x not in graph or y not in graph:
                return -1
            
            if y in graph[x]:
                return graph[x][y]

            for component in graph[x]:
                if component not in visited:
                    visited.add(component)
                    tempt = dfs(component, y, visited)
                    if tempt == -1:
                        continue
                    else:
                        return tempt * graph[x][component]
            return -1

        output = []

        for p,q in queries:
            output.append(dfs(p, q, set()))

        return output


from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1: Construct the graph
        graph = defaultdict(list)
        
        for i, equation in enumerate(equations):
            x, y = equation
            graph[x].append([y, values[i]])
            graph[y].append([x, 1 / values[i]])

        # Step 2: Define the BFS function
        def bfs(src, target):
            # If either the source or target does not exist in the graph
            if src not in graph or target not in graph:
                return -1

            # Initialize BFS with the source node and a weight of 1
            dq = deque([(src, 1)])
            visited = set([src])

            # Perform BFS
            while dq:
                cur, weight = dq.popleft()

                # If we reach the target node, return the accumulated weight
                if cur == target:
                    return weight

                # Explore the neighbors
                for nei, moreweight in graph[cur]:
                    newWeigh = weight * moreweight
                    if nei == target:
                        return newWeigh
                    
                    # Continue exploring if the neighbor hasn't been visited yet
                    if nei not in visited:
                        visited.add(nei)
                        dq.append((nei, newWeigh))

            # Return -1 if no valid path is found
            return -1

        # Step 3: Process all the queries
        return [bfs(x, y) for x, y in queries]