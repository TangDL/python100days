import sys

def helper(n, start, end, board, visited, res, count):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    print(start, end)
    if start == end:
        res.append(count)
    for i in range(4):
        new_x, new_y = start[0] + directions[i][0], start[1] + directions[i][1]
        if new_x >= 0 and new_x < n and new_y >= 0 and new_y < n and visited[new_x][new_y] != 1 and board[new_x][new_y] != '#' and board[new_x][new_y] != '@':
            visited[new_x][new_y] = 1
            count += 1
            helper(n, [new_x, new_y], end, board, visited, res, count)
            visited[new_x][new_y] = 0
            count -= 1


if __name__=="__main__":
    n = int(sys.stdin.readline().strip())
    temp = list(map(int, sys.stdin.readline().strip().split()))
    begin, end = [temp[0], temp[1]], [temp[2], temp[3]]

    board = []
    for i in range(n):
        board.append(sys.stdin.readline().strip())
    visited = [[0]*n]*n
    res = []
    ress = min(helper(n, begin, end, board, visited, res, 0))
    sys.stdout.write("d"%ress)