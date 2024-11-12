class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        dq = defaultdict(deque)
        substr = 0

        for i, x in enumerate(nums):
            dq[x].append(i)

            while dq[x][-1] - len(dq[x]) + 1 > len(dq[x]) + k:
                dq[x].popleft()

            substr = max(substr, len(dq[x]))

        return substr



        # indices = defaultdict(deque)
        # ans = 0
        
        # for i, x in enumerate(nums):
        #     indices[x].append(i)
            
        #     while indices[x][-1] - indices[x][0] + 1 > len(indices[x]) + k:
        #         indices[x].popleft()
                
        #     ans = max(ans, len(indices[x]))
        
        # return ans
        