class NumMatrix:
    
    def sumS(self, mat):
        rowSum = [[0]*len(mat[0]) for _ in range(len(mat))]
        for r in range(len(mat)):
            prevSum = 0
            for c in range(len(mat[0])):
                rowSum[r][c] = prevSum + mat[r][c]
                prevSum = rowSum[r][c]
        return rowSum
    
    def UpsumS(self, mat, row, col, diff):
        for c in range(col, len(mat[0])):
            mat[row][c] -= diff 

        return mat

        
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rowSum = self.sumS(matrix)
        

    def update(self, row: int, col: int, val: int) -> None:
        diff = self.matrix[row][col]  - val 
        self.matrix[row][col] = val
        self.rowSum = self.UpsumS(self.rowSum, row, col, diff)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        final = 0
        for r in range(row1, row2+1):
            final += self.rowSum[r][col2] if col1 == 0 else self.rowSum[r][col2] - self.rowSum[r][col1-1]
        
        return final
            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)