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
    

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        mem = {}
        def power(num):
            if num == 1:
                return 0 
            if num in mem:
                return mem[num]

            if num % 2 == 0:
                mem[num] = 1 + power(num // 2)
            else:
                mem[num] = 1 + power(3 * num + 1)

            return mem[num]

        res = [(i, power(i)) for i in range(lo, hi + 1)]
        res.sort(key=lambda x: (x[1], x[0]))

        return res[k - 1][0]

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        mem = {}
        def getPower(x):
            if x in mem:
                return mem[x]
            if x == 1:
                return 0
            elif x % 2 == 0:
                mem[x] =  1 + getPower(x // 2)
            else:
                mem[x] =  1 + getPower(3 * x + 1)
            
            return mem[x]

        powers = [(x, getPower(x)) for x in range(lo, hi + 1)]
        powers.sort(key = lambda x: (x[1], x[0]))

        return powers[k-1][0]

"""
Revised Complexity Analysis

Therefore, the actual time complexity is:

	•	Power Calculation: Each calculation generally takes  O(\log x)  transformations for a given  x , but the memoization optimizes repeated calculations. This step is difficult to define with exact asymptotic complexity but is generally efficient.
	•	Sorting:  O(n \log n) , where  n = \text{hi} - \text{lo} + 1 .

So, the overall complexity is close to  O(n \log n)  for the sorting part, with additional overhead for the power calculations, optimized through memoization.
"""

















        # mem = {}
        # def power(num):
        #     if num == 1:
        #         return 0 
        #     if num in mem:
        #         return mem[num]

        #     if num % 2 == 0:
        #         mem[num] = 1 + power(num // 2)
        #     else:
        #         mem[num] = 1 + power(3 * num + 1)

        #     return mem[num]

        # res = [(i, power(i)) for i in range(lo, hi + 1)]
        # res.sort(key=lambda x: (x[1], x[0]))

        # return res[k - 1][0]


         