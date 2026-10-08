def is_safe(board, row, col):
    for previous_row in range(row):
        previous_col = board[previous_row]

        if previous_col == col:
            return False

        if abs(previous_col - col) == abs(previous_row - row):
            return False

    return True

def solve_queens(board, row):
    if row == 8:
        return True

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col

            if solve_queens(board, row + 1):
                return True

            board[row] = -1

    return False

board = [-1] * 8
solve_queens(board)

print("8-Queens Solution:")
for row in range(8):
    line = ["."] * 8
    line[board[row]] = "Q"
    print(" ".join(line))
