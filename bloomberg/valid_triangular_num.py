class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        nums.sort()
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                k = i + 2
                for j in range(i + 1, len(nums)):
                    while k < len(nums) and nums[i] + nums[j] > nums[k]:
                        k += 1
                    count += k - j - 1

        return count



class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for k in range(len(nums) - 1, 1, -1):
            i = 0
            j = k - 1

            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                else:
                    i += 1

        return count



"""

TIME: O(N^2) + 0(NLOGN) =  O(N^2)
SPACE: 0(1) -> HEAP SORT INCURS NO EXTRA SPACE

"""



class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        output = 0

        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1

            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    output += right - left
                    right -= 1
                else:
                    left += 1

        return output

        # for k in range(len(nums) - 1, 1, -1):
        #     i = 0
        #     j = k - 1

        #     while i < j:
        #         if nums[i] + nums[j] > nums[k]:
        #             count += j - i
        #             j -= 1
        #         else:
        #             i += 1

        # return count



"""

TIME: O(N^2) + 0(NLOGN) =  O(N^2)
SPACE: 0(1) -> HEAP SORT INCURS NO EXTRA SPACE

"""