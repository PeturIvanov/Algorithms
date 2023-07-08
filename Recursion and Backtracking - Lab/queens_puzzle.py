def place_queen(r, c, b, rows, cols, left_diagonal, right_diagonal):
    b[r][c] = "*"
    rows.add(r)
    cols.add(c)
    left_diagonal.add(r - c)
    right_diagonal.add(r + c)


def print_board(board):
    for row in board:
        print(' '.join(row))
    print()


def remove_queen(row, col, board, rows, cols, left_diagonal, right_diagonal):
    board[row][col] = "-"
    rows.remove(row)
    cols.remove(col)
    left_diagonal.remove(row - col)
    right_diagonal.remove(row + col)


def can_place_queen(row, col, rows, cols, left_diagonal, right_diagonal):
    if row in rows:
        return False

    if col in cols:
        return False

    if row - col in left_diagonal:
        return False

    if row + col in right_diagonal:
        return False

    return True

def set_queens(row, board, rows, cols, left_diagonal, right_diagonal):
    if row == 8:
        print_board(board)
        return

    for col in range(8):
        if can_place_queen(row, col, rows, cols, left_diagonal, right_diagonal):
            place_queen(row, col, board, rows, cols, left_diagonal, right_diagonal)
            set_queens(row + 1, board, rows, cols, left_diagonal, right_diagonal)
            remove_queen(row, col, board, rows, cols, left_diagonal, right_diagonal)



board = [list("-" * 8) for _ in range(8)]
set_queens(0, board, set(), set(), set(), set())