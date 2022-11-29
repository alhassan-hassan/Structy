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