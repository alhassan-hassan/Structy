class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        paths = collections.defaultdict(list)
        res = []
        
        for i in range(len(edges)):
            first, second = edges[i]
            paths[first].append([second, succProb[i]])
            paths[second].append([first, succProb[i]])

        pq = [(-1, start_node)]
        visited = set()

        while pq:
            prob, cur = heapq.heappop(pq)
            visited.add(cur)

            if cur == end_node:
                return prob * -1

            for node, newProb in paths[cur]:
                if node not in visited:
                    curProb = prob * newProb
                    heapq.heappush(pq, (curProb, node))

        return 0
        