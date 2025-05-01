import tkinter as tk
from tkinter import messagebox

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_buttons()
        self.create_buttonsm()

    def create_grid(self):
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(self.root, width=3, font=('Arial', 18), justify='center')
                entry.grid(row=row, column=col, padx=1, pady=1)
                self.entries[row][col] = entry

    def create_buttons(self):
        solve_btn = tk.Button(self.root, text="Solve", command=self.solve)
        solve_btn.grid(row=9, column=3, columnspan=3, pady=10)
        
    def create_buttonsm(self):
        reset = tk.Button(self.root, text="Reset", command=self.reset)
        reset.grid(row=9, column=4, columnspan=5, pady=15)
        


    def get_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.entries[i][j].get()
                row.append(int(val) if val.isdigit() else 0)
            board.append(row)
        return board

    def set_board(self, board):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if board[i][j] != 0:
                    self.entries[i][j].insert(0, str(board[i][j]))

    def solve(self):
        board = self.get_board()
        if self.backtrack(board):
            self.set_board(board)
        else:
            messagebox.showerror("No Solution", "This Sudoku puzzle cannot be solved.")

    def find_empty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None
    
    def reset(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
        

    def is_valid(self, board, num, pos):
        row, col = pos

        if any(board[row][i] == num for i in range(9) if i != col):
            return False
        if any(board[i][col] == num for i in range(9) if i != row):
            return False

        box_x = col // 3
        box_y = row // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def backtrack(self, board):
        empty = self.find_empty(board)
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if self.is_valid(board, num, (row, col)):
                board[row][col] = num
                if self.backtrack(board):
                    return True
                board[row][col] = 0
        return False

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()