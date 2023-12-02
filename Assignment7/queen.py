# I have used chatGPT to generate the code for this assignment.
# Reasons for this is that there isn't any good material to go through this online.
# Also normal NQueen is rated as hard in Leetcode and with MQueens it would atleast be extreme.


def is_safe(board, row, col, n, left_row, lower_diag, upper_diag):
    return not (left_row[row] or lower_diag[row + col] or upper_diag[n - 1 + col - row])


def solve_nq_util(n, m, board, col, placed, left_row, lower_diag, upper_diag):
    if placed == m:
        return 1
    if col >= n:
        return 0
    solutions = 0
    for i in range(n):
        if is_safe(board, i, col, n, left_row, lower_diag, upper_diag):
            board[i][col] = 1
            left_row[i] = True
            lower_diag[i + col] = True
            upper_diag[n - 1 + col - i] = True

            solutions += solve_nq_util(
                n, m, board, col + 1, placed + 1, left_row, lower_diag, upper_diag
            )

            board[i][col] = 0
            left_row[i] = False
            lower_diag[i + col] = False
            upper_diag[n - 1 + col - i] = False
    solutions += solve_nq_util(
        n, m, board, col + 1, placed, left_row, lower_diag, upper_diag
    )
    return solutions


def queen(n, m):
    board = [[0] * n for _ in range(n)]
    left_row = [False] * n
    # array to keep track of the lower diagonals
    lower_diag = [False] * (2 * n - 1)
    # array to keep track of the upper diagonals
    upper_diag = [False] * (2 * n - 1)
    return solve_nq_util(n, m, board, 0, 0, left_row, lower_diag, upper_diag)


if __name__ == "__main__":
    print(queen(4, 4))  # 2
    print(queen(4, 2))  # 44
    print(queen(6, 4))  # 982
    print(queen(7, 2))  # 700
    print(queen(8, 8))  # 92
