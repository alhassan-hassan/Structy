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