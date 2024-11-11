import heapq
from typing import List, Tuple

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        startX, startY = start
        targetX, targetY = target
        
        # Priority queue for Dijkstra's algorithm (min-heap)
        pq = [(0, startX, startY)]  # (cost, x, y)
        
        # Dictionary to store minimum cost to reach each point
        min_cost = {(startX, startY): 0}
        
        while pq:
            cost, x, y = heapq.heappop(pq)
            
            # If we've reached the target, return the cost
            if (x, y) == (targetX, targetY):
                return cost
            
            # Consider moving directly to the target
            direct_cost = cost + abs(targetX - x) + abs(targetY - y)
            if (targetX, targetY) not in min_cost or direct_cost < min_cost[(targetX, targetY)]:
                min_cost[(targetX, targetY)] = direct_cost
                heapq.heappush(pq, (direct_cost, targetX, targetY))
            
            # Consider each special road
            for x1, y1, x2, y2, road_cost in specialRoads:
                # Cost to go from (x, y) to (x1, y1), then use the special road to (x2, y2)
                to_start_road_cost = cost + abs(x1 - x) + abs(y1 - y)
                new_cost = to_start_road_cost + road_cost
                
                # Only push if it's cheaper to reach (x2, y2) this way
                if (x2, y2) not in min_cost or new_cost < min_cost[(x2, y2)]:
                    min_cost[(x2, y2)] = new_cost
                    heapq.heappush(pq, (new_cost, x2, y2))
        
        return -1  # This line should not be reached due to problem constraints

import heapq
from typing import List, Tuple

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        stx, sty = start
        tgx, tgy = target

        queue = [(0, stx, sty)]
        minCost = {(stx, sty) : 0}

        while queue:
            cost, x, y = heapq.heappop(queue)
            if (x, y) == (tgx, tgy):
                return cost

            directDistance = cost + abs(tgx - x) + abs(tgy - y)
            if (tgx, tgy) not in minCost or directDistance < minCost[(tgx, tgy)]:
                minCost[(tgx, tgy)] = directDistance
                heapq.heappush(queue, (directDistance, tgx, tgy))

            for x1, y1, x2, y2, specialCost in specialRoads:
                specialDistance = cost + abs(x1 - x) + abs(y1 - y)
                specialDistance += specialCost
                if (x2, y2) not in minCost or specialDistance < minCost[(x2, y2)]:
                    minCost[(x2, y2)] = specialDistance
                    heapq.heappush(queue, (specialDistance, x2, y2))

        return -1