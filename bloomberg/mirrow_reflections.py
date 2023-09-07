class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        """
        If you carefully run a simulation, it is obvious that, there are some patterns that can be utilised

        if both p and q are odd. return 1
        if p is even and q is odd, return 2
        if p is odd and q is even, return 0

        """
        # In each condition, at least one of the numbers should be odd else -1 will be returned.
        # Hence, remove the two factors till at least one of the dimentions is odd.
        while p % 2 == 0 and q % 2 == 0:
            p /= 2
            q /= 2

        if p % 2 != 0 and q % 2 != 0:
            return 1
        if p % 2 ==0 and q % 2 != 0:
            return 2
        if p % 2 != 0 and q % 2 == 0:
            return 0
        return -1
    
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        """
        If you carefully run a simulation, it is obvious that, there are some patterns that can be utilised

        if both p and q are odd. return 1
        if p is even and q is odd, return 2
        if p is odd and q is even, return 0

        """
        # In each condition, at least one of the numbers should be odd else -1 will be returned.
        # Hence, remove the two factors till at least one of the dimentions is odd.
        while p % 2 == 0 and q % 2 == 0:
            p /= 2
            q /= 2

        if p % 2 == 0:
            return 2
        elif q % 2 == 0:
            return 0
        else:
            return 1