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

