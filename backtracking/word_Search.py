class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if ((r < 0 or c < 0) or (r >= ROWS  or c >= COLS) or
                (r,c) in visited or board[r][c] != word[i]):
                return False

            visited.add((r, c))

            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or \
                  dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)

            visited.remove((r, c))

            return res

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True

        return False
            

# TIME - O(N * M * 4^len(word))
"""
    we are calling the dfs four times on the total call stack of the code which is the length of the word.
    But one could argue that it's 3^len(word), since we actually explore 3 directions instead of 4 because we 
"""