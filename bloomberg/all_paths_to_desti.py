class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        start = 0
        target = len(graph) - 1
        res = []

        def dfs(curNode, path):
            if curNode == target:
                res.append(list(path))
                return

            for neighbour in graph[curNode]:
                path.append(neighbour)
                dfs(neighbour, path)
                path.pop()

        dfs(0, [start])

        return res

"""
    Complexity Analysis

	•	Time Complexity:
	•	In the worst case, we need to explore all paths from 0 to n-1, which could result in O(2^n) paths if each node has two outgoing edges. This gives an exponential time complexity due to the potential number of paths in the graph.
	•	Space Complexity:
	•	Auxiliary Space: The recursion depth can go up to O(n), where n is the number of nodes, because we could potentially go as deep as all nodes in the longest path. Each path in the result also takes space, resulting in O(2^n * n) space in the worst case.
	•	Result Storage: We store each path in res, leading to O(2^n * n) space for all possible paths.

    Code Explanation

"""




















        # begin = 0
        # trg = len(graph) - 1
        
        # res = []

        # def dfs(cur, path):
        #     if cur == trg:
        #         # create a copy of the list and append it to the result
        #         res.append(list(path))
        #         return

        #     for neighbor in graph[cur]:
        #         path.append(neighbor)
        #         dfs(neighbor, path)
        #         path.pop()

        # path = [0]
        # dfs(begin,path)

        # return res

