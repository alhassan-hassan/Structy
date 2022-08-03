class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        def getNext(n):
            total = 0
            
            while n > 0:
                quo, rem = divmod(n, 10)
                total += rem ** 2
                n = quo
            return total
        
        slow = n
        fast = getNext(n)
        
        while fast != 1 and fast != slow:
            slow = getNext(slow)
            fast = getNext(getNext(fast))
            
        return fast == 1