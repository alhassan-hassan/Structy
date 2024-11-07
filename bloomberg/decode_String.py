class Solution:
    def decodeString(self, s: str) -> str:
        # Use a stack to keep track of everything
        stack = []
        for char in s:
            # If a value is a closing brace, I will just uncompress the previous chars
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
        

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                count = ""

                while stack and stack[-1].isnumeric():
                    count = stack.pop() + count

                stack.append(int(count) * substr)

        return "".join(stack)
    


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                
                stack.pop()

                count = ""
                while stack and stack[-1].isnumeric():
                    count = stack.pop() + count
                
                stack.append(int(count) * substr)

        return "".join(stack)



        # stack = []

        # for i in range(len(s)):
        #     if s[i] != "]":
        #         stack.append(s[i])
        #     else:
        #         substr = ""
        #         while stack[-1] != "[":
        #             substr = stack.pop() + substr
        #         stack.pop()

        #         count = ""

        #         while stack and stack[-1].isnumeric():
        #             count = stack.pop() + count

        #         stack.append(int(count) * substr)

        # return "".join(stack)