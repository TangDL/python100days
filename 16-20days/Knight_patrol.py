import sys
import time
SIZE = 5
total = 0

def print_board(board):
    for row in board:
        for col in row:
            print(str(col).center(4), end='')
        print()

def patrol(board, row, col, step=1):
    if row>=0 and row<SIZE and col>=0 and col<SIZE and board[row][col] == 0:
        board[row][col] = step
        if step == SIZE*SIZE:
            global total
            total += 1
            print(f'it the {total}th patrol way:')
            print_board(board)
        # 下一步可能会走的位置
        patrol(board, row - 2, col + 1, step + 1)
        patrol(board, row - 2, col - 1, step + 1)
        patrol(board, row + 2, col + 1, step + 1)
        patrol(board, row + 2, col - 1, step + 1)
        patrol(board, row - 1, col + 2, step + 1)
        patrol(board, row - 1, col - 2, step + 1)
        patrol(board, row + 1, col + 2, step + 1)
        patrol(board, row + 1, col - 2, step + 1)
        # 以上的位置均走不通时，回退
        board[row][col] = 0                           # 此时board[row][col]代表倒数第2步，在该位置上述8种走法都试了之后，
                                                      # 将这个位置释放，回到倒数第3步，继续选择一种走法进行遍历
                                                      # 所以考虑这种问题的关键是，直接跳到最后一步，查看最后一步完成之后，应当怎么走


def main():
    board = [[0]*SIZE for _ in range(SIZE)]
    patrol(board, 0, 0)

if __name__=='__main__':
    main()