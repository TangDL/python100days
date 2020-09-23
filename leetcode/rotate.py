class Solution:
    def rotate(self, matrix) -> None:
        row = len(matrix)
        column = len(matrix[0])
        pos1, pos2 = 0, row-1

        while pos1<pos2:
            add = 0
            while add < pos2 - pos1:
                temp = matrix[pos1][pos1+add]
                matrix[pos1][pos1+add] = matrix[pos2-add][pos1]
                matrix[pos2-add][pos1] = matrix[pos2][pos2-add]
                matrix[pos2][pos2-add] = matrix[pos1+add][pos2]
                matrix[pos1+add][pos2] = temp
                add += 1
            pos1 += 1
            pos2 -= 1