class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        tempt = []
        for i in range(len(s)):
            if tempt and s[i] == tempt[-1][0]:
                tempt[-1][1] += 1
                if tempt[-1][1] == k:
                    tempt.pop()
            else:
                tempt.append([s[i], 1])
                    
        return ''.join(key * val for key, val in tempt)




# BETTER WAY
        # if len(s) < k: return s
            
        # tempt = s
        # stack = []
        
        # P1 = 0
        
        # while p1 < len(tempt):
        #     if p1 == 0 or tempt[p1] == tempt[p1-1]:
        #         stack.append(1)
        #         p1 += 1
        #     else:
        #         last = stack.pop() + 1
        #         stack.append(last)
                
        #         if last == k:
        #             tempt = tempt[0: p1 - k + 1] + tempt[p1 + 1 : ]
        #             p1 = p1 - k + 1
                    
        # return tempt
                
                
            