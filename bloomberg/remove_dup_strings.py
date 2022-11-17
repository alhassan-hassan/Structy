class Solution:
    def removeDuplicates(self, s, k):
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
                
            
        