class Solution:   #    TIME LIMIT EXCEEDED
    def isPossible(self, target: List[int]) -> bool:
        # if len(target) == 1:
        #     return target == [1]

        # sum_ = sum(target)

        # target = [-num for num in target]
        # heapq.heapify(target)

        # while -target[0] > 1:
        #     largest = -target[0]
        #     x = largest - (sum_ - largest)
        #     if x < 1:
        #         return False

        #     heapq.heapreplace(target, -x)
        #     sum_ = sum_ - largest + x

        # return True
        "Time Complexity : O(n+k log⁡ n)O(n + k \, \log \, n)O(n+klogn). LINEAR FOR SPACE"

    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target == [1]

        sum_ = sum(target)

        target = [-num for num in target]
        heapq.heapify(target)

        while -target[0] > 1:
            largest = -target[0]
            rest = sum_ - largest

            # This will only occur if n = 2.
            if rest == 1:
                return True

            x = largest % rest

            # If x is now 0 (invalid) or didn't
            # change, then we know this is impossible.
            if x == 0 or x == largest:
                return False

            heapq.heapreplace(target, -x)
            sum_ = sum_ - largest + x

        return True

"""
Time Complexity : O(n+log⁡ k⋅log⁡ n)O(n + \log \, k \cdot \log \, n)O(n+logk⋅logn).

Creating a heap is O(n)O(n)O(n).

At each step, we were removing at least 14\frac{1}{4} 
4
1
​
  of the total sum. The original total sum is 2⋅k2 \cdot k2⋅k, because kkk is the largest element, and we know that if the algorithm continues, then the rest can't add up to more than kkk. So, we need to take O(log⁡ k)O(\log \, k)O(logk) steps to reduce the array down. Each of these steps is the cost of a heap add and remove, i.e. O(log⁡ n)O(\log \, n)O(logn). In total, this is O(log⁡ k⋅log⁡ n)O(\log \, k \cdot \log \, n)O(logk⋅logn).

Space Complexity : O(n)O(n)O(n).
"""