class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # error checking
        if not board:
            return board

        done = True

        # check rows
        for r in range(len(board)):
            for c in range(len(board[0]) - 2):
                num1 = abs(board[r][c])
                num2 = abs(board[r][c + 1])
                num3 = abs(board[r][c + 2])

                if num1 == num2 and num2 == num3 and num2:
                    done = False
                    board[r][c] = board[r][c + 1] = board[r][c + 2] = -abs(num1)
       
        # check cols
        for c in range(len(board[0])):
            for r in range(len(board) - 2):
                num1 = abs(board[r][c])
                num2 = abs(board[r + 1][c])
                num3 = abs(board[r + 2][c])

                if num1 == num2 and num2 == num3 and num2:
                    done = False
                    board[r][c] = board[r + 1][c] = board[r + 2][c] = -abs(num1)

        # gravity
        if not done:
            for c in range(len(board[0])):
                ind = len(board) - 1

                for r in range(len(board) - 1, -1, -1):
                    if board[r][c] > 0:
                        board[ind][c] = board[r][c]
                        ind -= 1

                for r in range(ind, -1, -1):
                    board[r][c] = 0

        return board if done else self.candyCrush(board)
        

"""
    Let m×nm \times nm×n be the size of the grid board.

    Time complexity: O(m2⋅n2)O(m^2 \cdot n^2)O(m 
    2
    ⋅n 
    2
    )

    Each find_and_crush process takes O(m⋅n)O(m \cdot n)O(m⋅n) time as we need to iterate over every cell of board.
    There could be at most O(m⋅n)O(m \cdot n)O(m⋅n) independent drop steps to eliminate all valid candy groups.
    In summary, the time complexity in the worst-case scenario is O(m2⋅n2)O(m^2 \cdot n^2)O(m 
    2
    ⋅n 
    2
    ).
    Space complexity: O(1)O(1)O(1)

    Both the function drop and find_and_crush involve in-place modification and do not require additional space.

"""