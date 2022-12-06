class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        begin = 0
        target = len(graph) - 1

        res = []

        def backtrack(cur_node, path):
            if cur_node == target:
                print(path)
                res.append(list(path))
                return

            for neighbor in graph[cur_node]:
                path.append(neighbor)
                backtrack(neighbor, path)
                path.pop()

        path = [0]

        backtrack(begin, path)

        return res

        