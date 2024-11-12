class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, index):
            if index == len(word):
                return True
            
            if c < 0 or c >= COLS or r < 0 or r >= ROWS or board[r][c] != word[index] or (r,c) in visited:
                return False

            visited.add((r, c))
            # tempt = board[r][c]
            # board[r][c] = "#"

            found = (dfs(r + 1, c, index + 1) or dfs(r - 1, c, index + 1) or dfs(r, c + 1, index + 1) or dfs(r, c - 1, index + 1))
            
            visited.remove((r, c))
            # board[r][c] = tempt

            return found

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True

        return False



        # visited = set()

        # def dfs(r, c, i):
        #     if i == len(word):
        #         return True

        #     if ((r < 0 or c < 0) or (r >= ROWS  or c >= COLS) or
        #         (r,c) in visited or board[r][c] != word[i]):
        #         return False

        #     visited.add((r, c))

        #     res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or \
        #           dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)

        #     visited.remove((r, c))

        #     return res

        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if dfs(i, j, 0):
        #             return True

        # return False
            

        

"""
    Time Complexity

        1.	Outer Loop: We iterate over each cell in the grid (board), which has  \text{ROWS} \times \text{COLS}  cells. So, the outer loop contributes  O(\text{ROWS} \times \text{COLS}) .
        2.	DFS Recursion: For each cell, we initiate a Depth-First Search (DFS) with up to 4 possible directions (up, down, left, right). As discussed earlier, after the first move, the effective branching factor is 3 since we avoid revisiting the cell we came from.
        3.	Depth of DFS: The DFS will attempt to find a path that matches the length of the word, so the depth of recursion can go up to  L , where  L  is the length of the word.

    Therefore, the time complexity can be approximated as:

    O(\text{ROWS} \times \text{COLS} \times 3^L)

    Here:

        •	 \text{ROWS} \times \text{COLS}  is the cost of iterating over each cell to start a DFS.
        •	 3^L  is the approximate number of recursive calls made in each DFS, given the branching factor of 3 and the recursion depth of  L .

    Space Complexity

        1.	Visited Set: The visited set keeps track of the cells in the current path to prevent revisiting cells in the same recursive call chain. At most, this set will hold up to  L  cells at a time (if the path being explored is as long as the word).
        •	Space complexity for the visited set is  O(L) , where  L  is the length of word.
        2.	Recursive Call Stack: The recursive DFS calls have a maximum depth of  L  (the length of word), so the space required for the call stack is also  O(L) .

    Therefore, the space complexity is:

    O(L)

    since both the visited set and the recursion stack use up to  O(L)  space.

    Summary

        •	Time Complexity:  O(\text{ROWS} \times \text{COLS} \times 3^L) 
        •	Space Complexity:  O(L) 
"""