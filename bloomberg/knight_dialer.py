class Solution:
    def knightDialer(self, n: int) -> int:
        calls = [1] * 10  # Initial ways to reach each digit with 1 move (itself)
        MOD = 10**9 + 7   # Modulo value for large numbers

        # Moves mapping for each digit on the keypad
        moves = [
            [4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9],
            [], [0, 1, 7], [2, 6], [1, 3], [2, 4]
        ]

        # Iterate from the 2nd to the nth move
        for _ in range(2, n + 1):
            new_calls = [0] * 10  # Initialize a new list for the current move
            for j in range(10):
                # Sum the counts of ways to reach each possible "jump" destination
                new_calls[j] = sum(calls[k] for k in moves[j]) % MOD
            calls = new_calls  # Update calls with new_calls for the next move

        # Sum up all ways to reach each digit with exactly n moves
        return sum(calls) % MOD
    
    

class Solution:
    def knightDialer(self, n: int) -> int:
        calls = [1] * 10

        MOD = 10**9 + 7

        for i in range(2, n+1):
            old_calls = calls.copy()

            calls[0] = old_calls[4] + old_calls[6]
            calls[1] = old_calls[6] + old_calls[8]
            calls[2] = old_calls[7] + old_calls[9]
            calls[3] = old_calls[4] + old_calls[8]
            calls[4] = old_calls[3] + old_calls[9] + old_calls[0]
            calls[5] = 0
            calls[6] = old_calls[7] + old_calls[1] + old_calls[0]
            calls[7] = old_calls[2] + old_calls[6]
            calls[8] = old_calls[1] + old_calls[3]
            calls[9] = old_calls[2] + old_calls[4]

        return sum(calls) % MOD
    

class Solution:
    def knightDialer(self, n: int) -> int:
        calls = [1] * 10
        MOD = 10**9 + 7

        for i in range(1, n):
            old_calls = calls.copy()

            calls[0] = old_calls[6] + old_calls[4]
            calls[1] = old_calls[8] + old_calls[6]
            calls[2] = old_calls[7] + old_calls[9]
            calls[3] = old_calls[8] + old_calls[4]
            calls[4] = old_calls[3] + old_calls[9] + old_calls[0]
            calls[5] = 0
            calls[6] = old_calls[1] + old_calls[7] + old_calls[0]
            calls[7] = old_calls[2] + old_calls[6]
            calls[8] = old_calls[3] + old_calls[1]
            calls[9] = old_calls[2] + old_calls[4]

        return sum(calls) % MOD