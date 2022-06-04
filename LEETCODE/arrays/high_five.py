import heapq
from collections import defaultdict

class Solution:
    def highFive(self, items):
        
        dic = {}
        output = []
        for scores in items:
            if scores[0] in dic:
                dic[scores[0]].append(scores[1])
            else:
                dic[scores[0]] = [scores[1]]
                
        for each in dic:
            dic[each].sort(reverse = True)
        
        for i in dic:
            output.append([i, sum(dic[i][0:5])// 5])
            
        output = sorted(output, key = lambda x : x[0])
        return output
        
        fives = defaultdict(list)
        output = []
        
        for scores in items:
            heapq.heappush(fives[scores[0]], scores[1])
            if len(fives[scores[0]]) > 5:
                heapq.heappop(fives[scores[0]])
                
        for score in sorted(fives.keys()):
            output.append([score, sum(fives[score]) // 5])
            
        return output
    
        
        