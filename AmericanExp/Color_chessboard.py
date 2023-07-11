class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        def getIndex(alpha):
            return ord(alpha) - 96

        alpha, digit = getIndex(coordinates[0]), int(coordinates[1])

        return (alpha + digit) % 2 == 1 