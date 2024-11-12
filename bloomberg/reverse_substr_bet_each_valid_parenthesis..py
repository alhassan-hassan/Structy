class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ")":
                subs = []
                while stack and stack[-1] != "(":
                    subs.append(stack.pop())

                stack.pop()

                stack.extend(subs)

            else:
                stack.append(char)

        return "".join(stack)
    
""""
Time Complexity: O(n), where n is the length of the input string s. We iterate through each character in the string once.
Space Complexity: O(n), where n is the length of the input string s. The stack can contain at most n characters.
"""