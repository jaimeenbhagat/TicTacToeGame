import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg='#333')

        # Game state variables
        self.current_player = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.player_x_wins = 0
        self.player_o_wins = 0
        self.draws = 0

        # UI Elements
        self.create_ui()

    def create_ui(self):
        # Scoreboard
        self.scoreboard_frame = tk.Frame(self.root, bg='#333')
        self.scoreboard_frame.pack(pady=10)

        self.current_player_label = tk.Label(self.scoreboard_frame, text=f"Current Player: {self.current_player}", font=('Helvetica', 20, 'bold'), fg='#FFD700', bg='#333')
        self.current_player_label.grid(row=0, column=0, columnspan=3)

        self.player_x_wins_label = tk.Label(self.scoreboard_frame, text=f"Player X Wins: {self.player_x_wins}", font=('Helvetica', 15), fg='#FFFFFF', bg='#333')
        self.player_x_wins_label.grid(row=1, column=0)

        self.player_o_wins_label = tk.Label(self.scoreboard_frame, text=f"Player O Wins: {self.player_o_wins}", font=('Helvetica', 15), fg='#FFFFFF', bg='#333')
        self.player_o_wins_label.grid(row=1, column=1)

        self.draws_label = tk.Label(self.scoreboard_frame, text=f"Draws: {self.draws}", font=('Helvetica', 15), fg='#FFFFFF', bg='#333')
        self.draws_label.grid(row=1, column=2)

        # Game board
        self.board_frame = tk.Frame(self.root, bg='#333')
        self.board_frame.pack()

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.board_frame, text='', font=('Helvetica', 20, 'bold'), width=5, height=2,
                                   bg='#1E90FF', fg='#FFFFFF',
                                   command=lambda row=i, col=j: self.click_button(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

    def click_button(self, row, col):
        if self.buttons[row][col]['text'] == '' and self.current_player:
            self.buttons[row][col]['text'] = self.current_player
            self.buttons[row][col].config(bg='#FFD700' if self.current_player == 'X' else '#FF6347')
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                if self.current_player == 'X':
                    self.player_x_wins += 1
                else:
                    self.player_o_wins += 1
                self.update_scoreboard()
                self.reset_game()
            elif self.is_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.draws += 1
                self.update_scoreboard()
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.current_player_label.config(text=f"Current Player: {self.current_player}")

    def check_winner(self):
        for row in self.buttons:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != '':
                return True
        for col in range(3):
            if self.buttons[0][col]['text'] == self.buttons[1][col]['text'] == self.buttons[2][col]['text'] != '':
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != '':
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != '':
            return True
        return False

    def is_draw(self):
        for row in self.buttons:
            for button in row:
                if button['text'] == '':
                    return False
        return True

    def reset_game(self):
        for row in self.buttons:
            for button in row:
                button['text'] = ''
                button.config(bg='#1E90FF')
        self.current_player = 'X'
        self.current_player_label.config(text=f"Current Player: {self.current_player}")

    def update_scoreboard(self):
        self.player_x_wins_label.config(text=f"Player X Wins: {self.player_x_wins}")
        self.player_o_wins_label.config(text=f"Player O Wins: {self.player_o_wins}")
        self.draws_label.config(text=f"Draws: {self.draws}")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
