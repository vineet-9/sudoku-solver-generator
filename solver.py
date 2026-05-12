GRID_SIZE = 9


def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))


def find_empty(board):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == 0:
                return row, col
    return None


def is_valid(board, num, pos):
    row, col = pos

    # Check row
    for i in range(GRID_SIZE):
        if board[row][i] == num and i != col:
            return False

    # Check column
    for i in range(GRID_SIZE):
        if board[i][col] == num and i != row:
            return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    empty = find_empty(board)

    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False