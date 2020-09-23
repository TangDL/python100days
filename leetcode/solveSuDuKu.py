from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(start):
            if start == total:
                return True
            k, l = start//9, start%9
            if board[k][l] != '.':
                return dfs(start+1)
            else:
                for i in range(1, 10):
                    if c_visited[l][i] or r_visited[k][i] or block_visited[k//3][l//3][i]:
                        continue
                    else:
                        board[k][l] = str(i)
                        c_visited[l][i] = True
                        r_visited[k][i] = True
                        block_visited[k//3][l//3][i] = True
                        if dfs(start+1): return True
                        board[k][l] = '.'
                        c_visited[l][i] = False
                        r_visited[k][i] = False
                        block_visited[k//3][l//3][i] = False


        total = len(board) * len(board[0])
        column = len(board[0])
        c_visited = [[False] * 10] * 9
        r_visited = [[False] * 10] * 9
        block_visited = [[[False] * 3]]*3 * 9
        for i in range(column):
            for j in range(column):
                if board[i][j] != '.':
                    c_visited[j][int(board[i][j])] = True
                    r_visited[i][int(board[i][j])] = True
                    block_visited[i//3][j//3][int(board[i][j])] = True
        dfs(0)

