class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        memo = {2:1}
        
        def dp (n):
            
            if n == 2:
                return 1
            
            if n in memo:
                return memo[n]
            
            cur = 0
            if n % 2 :
                cur = 1 + dp(3*n+1)
            else:
                cur = 1 + dp (n//2)
            
            memo[n] = cur
            
            return cur
        final = []
        for i in range(lo, hi+1):
            cur = dp(i)
            final.append([cur, i])
        
        final.sort(key = lambda x: x[0] )
        return final[k-1][1]