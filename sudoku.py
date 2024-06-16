import tkinter as tk
from tkinter import messagebox

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        
        self.grid = [[0]*9 for _ in range(9)]
        self.entries = [[None]*9 for _ in range(9)]
        
        self.create_widgets()
    
    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()
        
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(frame, width=2, font=('Arial', 18), justify='center')
                entry.grid(row=i, column=j, padx=5, pady=5)
                self.entries[i][j] = entry
        
        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.pack(pady=20)
    
    def read_grid(self):
        for i in range(9):
            for j in range(9):
                val = self.entries[i][j].get()
                if val.isdigit():
                    self.grid[i][j] = int(val)
                else:
                    self.grid[i][j] = 0

    def display_grid(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != 0:
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(self.grid[i][j]))

    def is_valid(self, grid, row, col, num):
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve_sudoku(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if self.solve_sudoku(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True
    
    def solve(self):
        self.read_grid()
        if self.solve_sudoku(self.grid):
            self.display_grid()
            messagebox.showinfo("Sudoku Solver", "Sudoku Solved!")
        else:
            messagebox.showerror("Sudoku Solver", "No solution exists")

if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuSolverGUI(root)
    root.mainloop()
