# utils.py

GRID_SIZE = 9


def print_board(board):
    """
    Prints the Sudoku board in a readable format.
    """
    for i in range(GRID_SIZE):

        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(GRID_SIZE):

            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def is_board_full(board):
    """
    Checks if the Sudoku board is completely filled.
    """
    for row in board:
        if 0 in row:
            return False
    return True


def copy_board(board):
    """
    Returns a deep copy of the Sudoku board.
    """
    return [row[:] for row in board]


def get_empty_positions(board):
    """
    Returns a list of empty cell positions.
    """
    empty_positions = []

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == 0:
                empty_positions.append((row, col))

    return empty_positions


def validate_board(board):
    """
    Validates the entire Sudoku board.
    """

    # Check rows
    for row in range(GRID_SIZE):
        nums = [num for num in board[row] if num != 0]

        if len(nums) != len(set(nums)):
            return False

    # Check columns
    for col in range(GRID_SIZE):
        nums = []

        for row in range(GRID_SIZE):
            if board[row][col] != 0:
                nums.append(board[row][col])

        if len(nums) != len(set(nums)):
            return False

    # Check 3x3 subgrids
    for box_row in range(0, GRID_SIZE, 3):
        for box_col in range(0, GRID_SIZE, 3):

            nums = []

            for i in range(3):
                for j in range(3):

                    num = board[box_row + i][box_col + j]

                    if num != 0:
                        nums.append(num)

            if len(nums) != len(set(nums)):
                return False

    return True