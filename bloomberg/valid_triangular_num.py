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