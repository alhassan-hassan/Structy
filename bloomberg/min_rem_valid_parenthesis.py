class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opened = closed = 0
        stack = []

        for char in s:
            if char == "(":
                stack.append(char)
                opened += 1
            
            elif char == ")":
                if closed < opened:
                    closed += 1
                    stack.append(")")
            else:
                stack.append(char)

        if opened == closed:
            print("hey")
            return "".join(stack)

        track = len(stack) - 1

        while track >= 0 and opened > closed:
            if stack[track] == "(":
                opened -= 1
                stack.pop(track)
            track -= 1

        print(stack)
        return "".join(stack)
    
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        rem = set()

        for i, c in enumerate(s):
            if c not in "()":
                continue

            if c == "(":
                stack.append(i)
            elif not stack:
                rem.add(i)
            else:
                stack.pop()

        rem = rem.union(set(stack))
        s_builder = []

        for ind, ch in enumerate(s):
            if ind not in rem:
                s_builder.append(ch)

        return "".join(s_builder)



        