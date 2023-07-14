class Solution:
    def intToRoman(self, num: int) -> str:
        notations = [
            ["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], \
            ["XC", 90], ["C", 100], ["CD", 400], ["D", 500],["CM", 900], ["M", 1000]
        ]

        res = ""

        for roman, numeral in reversed(notations):
            if num // numeral > 0:
                print([roman, numeral])
                count = num // numeral
                res += (count * roman)

                num = num % numeral

        return res
