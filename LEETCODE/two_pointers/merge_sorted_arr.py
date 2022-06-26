class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        tempt1 = nums1[ : m]
        
        def helperSort(temp1, nums2):
            p1 = p2 = 0
            final = []
            
            while p1 < len(temp1) and p2 < len(nums2):
                if temp1[p1] < nums2[p2]:
                    final.append(temp1[p1])
                    p1 += 1
                else:
                    final.append(nums2[p2])
                    p2 += 1
                    
            final.extend(temp1[p1:])
            final.extend(nums2[p2:])
            
            return final
            
        final = helperSort(tempt1, nums2)
        nums1[:] = final