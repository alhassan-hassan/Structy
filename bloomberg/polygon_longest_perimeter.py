class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum_ = sum(nums)

        for i in range(len(nums) - 1, 1, -1):
            sum_ -= nums[i]
            if sum_ > nums[i]:
                return sum_ + nums[i]

        return -1

        # BRUTEFORCE
        # Sort the side lengths in ascending order
        nums.sort()
        
        # Check for valid polygon starting from the largest possible triplet
        for i in range(len(nums) - 1, 1, -1):
            if sum(nums[0 : i]) > nums[i]:
                # Return the perimeter of this valid polygon
                return sum(nums[0 : i + 1])
        
        # Return -1 if no valid polygon can be formed
        return -1