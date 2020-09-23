import sys

def main():
    def dfs(x, y):
        if x < 0 or y < 0 or x >= m or y >= n or grid[y][x] == 'v' or grid[y][x] == '#':
            return False
        if grid[y][x] == 'E':
            return True

        grid[y][x] = 'v'
        for dir in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            new_x, new_y = x + dir[0], y + dir[1]
            if dfs(new_x, new_y): return True
        grid[y][x] = '.'
        return False


    T = int(sys.stdin.readline().strip())
    res = []
    for i in range(T):
        [n, m] = list(map(int, sys.stdin.readline().strip().split()))
        grid = []
        for i in range(n):
            grid.append(list(map(str, sys.stdin.readline().strip().split())))
        S_x, S_y = -1, -1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'S':
                    S_x, S_y = j, i

        if S_x==-1 or S_y==-1:
            res.append('No')
        if dfs(S_x, S_y):
            res.append('yes')
        else:
            res.append('No')
    for i in range(len(res)):
        sys.stdout.write('%s'%res[i])
        if i < len(res) -1:
            sys.stdout.write('\n')

if __name__=="__main__":
    main()

    """
    2
    3 3 
    . S .
    # # #
    E . .
    4 4
    . . . S
    # # # .
    # . . .
    E . . #
    """