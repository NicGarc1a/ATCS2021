import random


class ConnectFour:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = []
        self.columns = 8
        self.rows = 8

        for i in range(self.columns):
            row = []
            for t in range(self.rows):
                dash = "-"
                row.append(dash.strip())
            self.board.append(row)

    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("Rules of Connect Four: You can play another player or an AI on an 8X8 board")
        print("2)  to win, you must create a diagonal, horizontal, or vertical line of 4")
        print("3) the game ends when either player wins")

    def print_board(self):
        # TODO: Print the board
        print("   0 1 2 3 4 5 6 7")
        for t in range(self.columns):
            print(str(t), end='  ')
            print(*self.board[t])


    def is_valid_move(self, row, col):

    def place_player(self, player, row, col):


    def take_manual_turn(self, player):


    def take_turn(self, player):

    def check_col_win(self, player):
        # TODO: Check col win

    def check_row_win(self, player):

    def check_diag_win(self, player):

    def check_win(self, player):
        # TODO: Check win

        if(self.check_col_win(player) == True or self.check_row_win(player) == True or self.check_diag_win(player) == True):
            return True
        else:
            return False


    def check_tie(self):

    def statemachine(self, player):

    def take_statemachine_turn(self, player):

    def minimax(self, player, depth):

    def take_minimax_turn(self, player, depth):

    def play_game(self):
