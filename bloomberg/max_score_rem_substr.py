class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        firstPattern, firstScore = ("ab", x) if x > y else ("ba", y)
        secondPattern, secondScore = ("ba", y) if firstPattern == "ab" else ("ab", x)

        def scoreRemoval(chars, pattern, points):
            score = 0
            stack = []

            for char in chars:
                if stack and stack[-1] + char == pattern:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)

            return "".join(stack), score

        remainingChars, priorityScore = scoreRemoval(s, firstPattern, firstScore)
        _, remainingScore = scoreRemoval(remainingChars, secondPattern, secondScore)

        return priorityScore + remainingScore

"""
	•	Time Complexity:  O(n) , since each character is processed at most twice.
	•	Space Complexity:  O(n) , due to the use of a stack to keep track of characters during removal operations.

"""

        