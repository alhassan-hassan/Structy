class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(1, 10)]

        ans = []

        def dfs(count, num):
            if count == 0:
                return ans.append(num)

            tail_num = num % 10
            new_set = set([tail_num + k, tail_num - k])

            for builder in new_set:
                if 0 <= builder < 10:
                    new_num = num * 10 + builder
                    dfs(count - 1, new_num)

        for head in range(1, 10):
            dfs(n-1, head)

        return ans


"""
TIME:
    In the worst case, the total number of nodes in a binary tree of depth N−1N-1N−1 is 2N2^N2 N.
    Hence, the overall time complexity of the algorithm is O(2^N)
    ).


SPACE:
    Space Complexity:  O(2^N)
 )

Since we adopt a recursive solution, we would have some additional memory consumption on the function call stack. The maximum number of consecutive calls on the recursion function is N. Hence, the space complexity for the call stack is O(N).

We use a list to keep all the solutions, which could amount to 9⋅2^(N-1)
  number of elements.

To sum up, the overall space complexity of the algorithm is O(2^N)
"""
        