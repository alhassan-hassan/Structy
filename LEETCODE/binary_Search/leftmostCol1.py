# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def.o dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, columns = binaryMatrix.dimensions()
        indFinale = float("inf")
        for row in range(rows):
            ind = float("inf")
            low = 0
            high = rows
            
            while low < high:
                mid = (low + high) // 2
                if binaryMatrix.get(row, mid) == 1:
                    ind = min(ind, mid)
                    high = mid
                else:
                    low = mid + 1
            indFinale = min(indFinale, ind)
            
        return -1 if indFinale == float("inf") else indFinale
                
                    
                
        
                    
            
        