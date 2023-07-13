class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count, mapp = 0, collections.defaultdict(int)

        for num in time:
            if num % 60 == 0:
                count += mapp[0]
            
            else:
                comp = 60 - num % 60
                count += mapp[comp]
            
            mapp[num % 60] += 1

        return count




"""
TIME: O(N)
SPACE: 0(1)
"""

        