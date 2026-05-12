from solver import solve, print_board
from generator import generate_sudoku


def main():
    print("🧩 Sudoku Generator & Solver")
    print("1. Generate Sudoku")
    print("2. Solve Sudoku")

    choice = input("Enter your choice: ")

    if choice == "1":
        difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
        board = generate_sudoku(difficulty)

        print("\nGenerated Sudoku Puzzle:\n")
        print_board(board)

    elif choice == "2":
        print("Enter Sudoku row by row.")
        print("Use 0 for empty spaces.\n")

        board = []

        for i in range(9):
            row = list(map(int, input(f"Row {i + 1}: ").split()))
            board.append(row)

        print("\nOriginal Puzzle:\n")
        print_board(board)

        if solve(board):
            print("\nSolved Sudoku:\n")
            print_board(board)
        else:
            print("No solution exists.")

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()