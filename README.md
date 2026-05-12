# 🧩 Sudoku Solver & Generator

A project that can **solve Sudoku puzzles** and **generate new ones** with different difficulty levels. It demonstrates algorithmic problem-solving using backtracking and logical validation.

---

## 🚀 Features

* ✅ Solves any valid Sudoku puzzle
* 🎲 Generates new Sudoku boards
* 📊 Supports multiple difficulty levels (Easy, Medium, Hard)
* ⚡ Efficient backtracking algorithm
* 🧠 Ensures valid and unique solutions
* 💡 Clean and modular code structure

---

## 🛠️ Tech Stack

* Python
* Algorithms: Backtracking, Constraint Checking
* Libraries: (mention if used, e.g., numpy)

---

## 📂 Project Structure
sudoku-solver/
│── solver.py # Sudoku solving logic
│── generator.py # Puzzle generation logic
│── utils.py # Helper functions
│── main.py # Entry point
│── README.md # Project documentation


---


---

## 🧠 How It Works

### 🔹 Solver

* Finds empty cells in the grid
* Tries numbers from 1–9
* Checks validity (row, column, 3x3 box)
* Uses recursion and backtracking to solve

### 🔹 Generator

* Creates a complete valid Sudoku grid
* Removes numbers based on difficulty level
* Ensures the puzzle has a unique solution

---

## 📸 Example

Input:

5 3 . . 7 . . . .

6 . . 1 9 5 . . .

. 9 8 . . . . 6 .


Output:


5 3 4 6 7 8 9 1 2

6 7 2 1 9 5 3 4 8

1 9 8 3 4 2 5 6 7


---

## 🔍 Future Improvements

* 🌐 Web-based interface
* 🎨 GUI (Tkinter / React)
* 📱 Mobile app version
* ⏱️ Performance optimization
* 🧪 Unit testing

---

## 🤝 Contributors

* Vineet

---

## 📜 License

This project is for educational purposes. You can modify and use it freely.

---
