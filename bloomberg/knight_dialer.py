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