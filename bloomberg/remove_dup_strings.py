class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        d e e e d b b c c c b d a a
        
        [d, ]
        """
        if len(s) < k: return s
        
        stack = []
        
        for char in s:
            if len(stack) == 0 or stack[-1][0] != char:
                stack.append((char, 1))
            elif char == stack[-1][0]:
                stack.append((char, stack[-1][1] + 1))
                
            if stack[-1][1] == k:
                for i in range(k):
                    stack.pop()
        
        return "".join([x[0] for x in stack])



# BETTER WAY
        if len(s) < k: return s
            
        tempt = s
        stack = []
        
        P1 = 0
        
        while p1 < len(tempt):
            if p1 == 0 or tempt[p1] == tempt[p1-1]:
                stack.append(1)
                p1 += 1
            else:
                last = stack.pop() + 1
                stack.append(last)
                
                if last == k:
                    tempt = tempt[0: p1 - k + 1] + tempt[p1 + 1 : ]
                    p1 = p1 - k + 1
                    
        return tempt
                
                
            