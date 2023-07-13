# MINE
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        bodmas = collections.defaultdict(dict)
        res = []
        
        for i in range(len(equations)):
            first, second = equations[i]
            bodmas[first][second] = values[i]
            bodmas[second][first] = 1 / values[i]

        def dfs(query, visited):
            x, y = query

            if x not in bodmas or y not in bodmas:
                return -1

            if y in bodmas[x]:
                return bodmas[x][y]

            for neighbour in bodmas[x]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    nQuery = [neighbour, y]
                    tempt = dfs(nQuery, visited)

                    if tempt != -1:
                        return tempt * bodmas[x][neighbour]

            return -1

        for query in queries:
            res.append(dfs(query, set()))

        return res

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



# class Solution:
#     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
#         bodmas = collections.defaultdict(dict)
#         res = []
        
#         for i in range(len(equations)):
#             first, second = equations[i]
#             bodmas[first][second] = values[i]
#             bodmas[second][first] = 1 / values[i]

#         def dfs(query, val, visited):
#             x, y = query
#             if x not in bodmas or y not in bodmas:
#                 res.append(-1.0)
#                 return 

#             curBod = bodmas[x]
#             if y in curBod:
#                 val *= curBod[y]
#                 res.append(val)
#                 return
                
#             visited.add(x)
#             for other in curBod:
#                 if other not in visited:
#                     val *= bodmas[x][other]
#                     nQuery = [other, y]
#                     dfs(nQuery, val, visited)

#         for num in queries:
#             dfs(num, 1, set())

#         return res





        