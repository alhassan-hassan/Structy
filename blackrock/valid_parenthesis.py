class Solution:
    def isValid(self, s: str) -> bool:
        opns = []
        mts = {")" : "(", "}" : "{", "]" : "["}

        for char in s:
            if char in mts:
                ope = opns.pop() if opns else "!"
                if ope != mts[char]:
                    return False

            else:
                opns.append(char)

        return len(opns) == 0
