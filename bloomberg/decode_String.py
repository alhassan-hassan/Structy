class Solution:
    def decodeString(self, s: str) -> str:
        ["3[a"]
        
        stack = []
        res = []
        
        for char in s:
            if char != "]":
                stack.append(char)
                
            else:
                empt = ''
                while stack and stack[-1] != "[":
                    empt = stack.pop() + empt
                stack.pop()
                
                uncompress = ''
                while stack and stack[-1].isnumeric():
                    uncompress = stack.pop() + uncompress
                
                unzipped = int(uncompress) * empt 
                stack.append(unzipped)
                    
        return "".join(stack)