from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Special case: single element
        if len(nums) == 1:
            return nums[0]
        
        # Sort nums to handle negatives easily
        nums.sort()
        
        # Track the maximum product
        max_product = 1
        has_non_zero = False
        smallest_negative = None
        
        # Calculate the product, skipping one smallest negative if odd count
        for num in nums:
            if num != 0:
                max_product *= num
                has_non_zero = True
                if num < 0:
                    if smallest_negative is None or num > smallest_negative:
                        smallest_negative = num
        
        # If max_product is negative and we have odd number of negatives, 
        # divide by the smallest negative (remove it from the product)
        if max_product < 0 and smallest_negative is not None:
            max_product //= smallest_negative
        
        # Handle cases with all zeroes or single negative
        if not has_non_zero:
            return 0
        
        return max_product