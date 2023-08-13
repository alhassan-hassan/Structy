class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])

        # N^2
        self.board = [[0] * (COLS + 1) for row in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.board[r][c+1]
                self.board[r+1][c+1] = prefix + above

    def update(self, row: int, col: int, val: int) -> None:
        ROWS, COLS = len(self.board), len(self.board[0])
        diff = val - (self.board[row + 1][col + 1] - self.board[row][col + 1] - self.board[row + 1][col] + self.board[row][col])

        for r in range(row + 1, ROWS):
            for c in range(col + 1, COLS):
                self.board[r][c] += diff


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        cur_sum = self.board[row2][col2]
        above = self.board[row1 - 1][col2]
        left = self.board[row2][col1 - 1]
        leftTop = self.board[row1 - 1][col1 - 1]

        return cur_sum - above - left + leftTop

    # SPACE = N ^ 2