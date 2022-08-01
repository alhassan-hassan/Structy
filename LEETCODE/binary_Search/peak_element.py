class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
            nums = [1, 2 , 3 , 1]  
            
            lo = 0 and hi = 4
            mid = 4 + 0 // 2 = 2
            
            [1, 2 , 3 , 1]
            l       *   
                    h
            
                if mid id greater than the right neighbor:
                Update right pointer to the mid val
                
            [1, 2 , 3]
            *
                m   *
            mid = 0 + 2 // 2 = 1
            
            Here, the mid value is g
            Left = mid + 1
            
        """
        
        head = 0
        tail = len(nums) - 1      
        while head < tail:
            mid = (head + tail) // 2
            
            if nums[mid] > nums[mid + 1]:
                tail = mid
            else:
                head = mid + 1
                
        return head