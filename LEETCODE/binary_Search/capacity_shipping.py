class Solution:
    def shipWithinDays(self, weights, days):
        def isShippable(capacity):
            dayCount, curCapacity = 1, 0
            
            for weight in weights:
                if curCapacity + weight <= capacity:
                    curCapacity += weight
                else:
                    dayCount += 1
                    curCapacity = weight
                    
            return dayCount <= days
        
        minW, maxW = max(weights), sum(weights)
        
        while minW < maxW:
            mid = (minW + maxW) // 2
            
            if isShippable(mid):
                maxW = mid
            else:
                minW = mid + 1
                
        return minW