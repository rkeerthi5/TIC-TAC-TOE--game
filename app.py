import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("800x800")  # Set window size to 800x800
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        outer_frame = tk.Frame(self.root, bg="black")  # Outer frame with black background
        outer_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame in the window

        frame = tk.Frame(outer_frame)
        frame.pack()  # Pack the inner frame inside the outer frame

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(frame, text="", font=("Helvetica", 20), width=5, height=2, bd=4)  # setting border width
                self.buttons[i][j].config(command=lambda row=i, col=j: self.button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def button_click(self, row, col):
        if self.board[row][col] == "":
            self.buttons[row][col].config(text=self.current_player)
            if self.current_player == "X":
                self.buttons[row][col].config(bg="lightgreen")
            else:
                self.buttons[row][col].config(bg="lightblue")
            self.board[row][col] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Winner", "{} wins!".format(self.current_player))
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Draw", "The game is a draw!")
                self.reset_game()
            else:
                self.toggle_player()

    def toggle_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for row in self.board:
            if all(cell == self.current_player for cell in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == self.current_player for row in range(3)):
                return True
        if all(self.board[i][i] == self.current_player for i in range(3)) or \
           all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(cell != "" for row in self.board for cell in row)

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
                self.buttons[i][j].config(bg="SystemButtonFace")  # Reset button color
                self.board[i][j] = ""
        self.current_player = "X"

if __name__ == "__main__":
    game = TicTacToe()
    game.root.mainloop()
