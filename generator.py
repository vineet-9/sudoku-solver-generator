import random
from solver import is_valid

GRID_SIZE = 9


def generate_empty_board():
    return [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


def fill_board(board):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)

                for num in numbers:
                    if is_valid(board, num, (row, col)):
                        board[row][col] = num

                        if fill_board(board):
                            return True

                        board[row][col] = 0

                return False

    return True

def remove_numbers(board, difficulty="medium"):
    difficulty_levels = {
        "easy": 30,
        "medium": 40,
        "hard": 50
    }

    remove_count = difficulty_levels.get(difficulty, 40)

    while remove_count > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        if board[row][col] != 0:
            board[row][col] = 0
            remove_count -= 1

    return board


def generate_sudoku(difficulty="medium"):
    board = generate_empty_board()
    fill_board(board)
    remove_numbers(board, difficulty)
    return board