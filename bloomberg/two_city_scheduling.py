class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        diffs = []
        
        for c1, c2 in costs:
            diff = c1 - c2
            diffs.append([diff, c1, c2])
            
        diffs.sort()
        
        minCost = 0
        
        for i in range (len(diffs)):
            if i < len(diffs) // 2:
                minCost += diffs[i][1]
            else:
                minCost += diffs[i][2]
                
        return minCost
    

# NOW

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        greedy = [[x[0] - x[1], x[0], x[1]] for x in costs]

        greedy.sort()
        total = 0
   
        for i in range(len(greedy)):
            if i < len(greedy) // 2:
                total += greedy[i][1]
            else:
                total += greedy[i][2]

        return total
