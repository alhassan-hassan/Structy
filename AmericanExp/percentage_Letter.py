class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:

        letters = Counter(s)
        ratio = letters[letter] if letter in letters else 0

        return int((ratio / len(s)) * 100)