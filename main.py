import time
import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Крестики-нолики")

        self.turn = 'X'
        self.board = [['', '', ''] for i in range(3)]
        self.buttons = [[None for i in range(3)] for j in range(3)]

        self.draw_board()

    def draw_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text=self.board[i][j], font=('Arial', 60), bg='DeepPink', width=2, height=1,
                                   command=lambda row=i, col=j: self.button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button
                self.master.configure(bg='green')

    def button_click(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.turn
            button = self.buttons[row][col]
            button.config(text=self.turn, state='disabled', bg='DeepPink4')
            self.master.update()
            time.sleep(0.1)
            button.config(bg='pink')
            self.master.update()
            time.sleep(0.1)
            button.config(bg='DeepPink', state='normal')
            if self.check_win():
                tk.messagebox.showinfo('Победа!', f'Игрок {self.turn} победил!')
                self.reset()
            elif self.check_tie():
                tk.messagebox.showinfo('Ничья!', 'Ничья!')
                self.reset()
            else:
                self.turn = 'O' if self.turn == 'X' else 'X'


    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

    def check_tie(self):
        for row in self.board:
            for col in row:
                if col == '':
                    return False
        return True

    def reset(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ''
                self.buttons[i][j].config(text='')
        self.turn = 'X'


root = tk.Tk()
root.resizable(width=False, height=False)
game = TicTacToe(root)
root.mainloop()
