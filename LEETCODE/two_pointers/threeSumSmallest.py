class Solution:
    def threeSumSmaller(self, nums, target ):
        if len(nums) < 3:
            return 0
        
        nums.sort()
        print(nums)
        
        sml = 0
        
        for i in range(len(nums)):
            p1 = i + 1
            p2 = len(nums) - 1

            while p1 < p2:
                summ = nums[i] + nums[p1] + nums[p2]
                if summ < target:
                    sml += p2 - p1
                    p1 += 1
                elif summ >= target:
                    p2 -= 1
                       
        return sml

        