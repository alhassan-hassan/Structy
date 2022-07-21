class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
                     2 3 5 6
        nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
                 p1                            p2
 
        """
#         UISNG THREE POINTERS
        
    
        p1 = m - 1
        p2 = n - 1
        jp = m + n - 1
        for i in range(jp, -1, -1):
            if p1 >=0 and p2 >= 0:
                if nums1[p1] >= nums2[p2]:
                    nums1[i] = nums1[p1]
                    p1 -= 1
                else:
                    nums1[i] = nums2[p2]
                    p2 -= 1
            elif p1 >= 0:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
        print(nums1)
        
        
        
        
        
        
        
#         tempt = []
        
#         def merge():
#             p1 = p2 = 0
            
#             while p1 < m and p2 < len(nums2):
#                 if nums1[p1] < nums2[p2]:
#                     tempt.append(nums1[p1])
#                     p1 += 1
#                 else:
#                     tempt.append(nums2[p2])
#                     p2 += 1
                    
#             if p1 < m:
#                 tempt.extend(nums1[p1 : m])
                
#             if p2 < len(nums2):
#                 tempt.extend(nums2[p2 : ])
#             print(tempt)
#         merge()
#         nums1[ : ] = tempt
        
        
        