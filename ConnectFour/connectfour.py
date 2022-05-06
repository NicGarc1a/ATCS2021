import random


class ConnectFour:
    def __init__(self):
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
        print("Rules of Connect Four: You can play another player or an AI on an 8X8 board")
        print("2)  to win, you must create a diagonal, horizontal, or vertical line of 4")
        print("3) the game ends when either player wins")

    def print_board(self):
        print("   0 1 2 3 4 5 6 7")
        for t in range(self.columns):
            print(str(t), end='  ')
            print(*self.board[t])


    def is_valid_move(self, row, col):
        if (self.board[row][col] == '-'):
            return True
        return False

    def place_player(self, player, row, col):

        if (player == 0):
            self.board[row][col] = 'B'

        if (player == 1):
            self.board[row][col] = 'R'

        if (player == '-'):
            self.board[row][col] = '-'

    def take_manual_turn(self, player):

        while (True):
            try:
                full = True
                while(full == True):
                    colInput = int(input("What column to drop: "))
                    if (self.board[0][colInput] != '-'):
                        print("That row is full go again")
                    else:
                        full = False
                for i in range(7,-1,-1):
                    if (self.board[i][colInput] == '-'):
                        rowInput = i
                if (player == 0):
                    self.place_player(0, rowInput, colInput)
                elif (player == 1):
                    self.place_player(1, rowInput, colInput)

            except IndexError:
                print("this is not a valid response")
                continue
            except ValueError:
                print("this is not a valid response")
                continue
            return


    def take_turn(self, player):
        print()
        print("Player 1, take your turn:")
        self.take_manual_turn(player)

    def check_col_win(self, player):
        bstreak = 0
        rstreak = 0
        if (player == 0):
            for i in range(self.columns):
                for t in range(self.columns):
                    if self.board[t][i] == 'B':
                        bstreak = bstreak + 1
                    else:
                        bstreak = 0
                if (bstreak == 4):
                    print("Blue column win")
                    return True
        if (player == 1):
            for i in range(self.columns):
                for t in range(self.columns):
                    if self.board[t][i] == 'R':
                        rstreak = rstreak + 1
                    else:
                        rstreak = 0
                if (rstreak == 4):
                    print("Red column win")
                    return True

        return False

    def check_row_win(self, player):
        bstreak = 0
        rstreak = 0
        if (player == 0):
            for i in range(self.columns):
                for t in range(self.columns):
                    if self.board[i][t] == 'B':
                        bstreak = bstreak + 1
                    else:
                        bstreak = 0
                if (bstreak == 4):
                    print("Blue row win")
                    return True
        if (player == 1):
            for i in range(self.columns):
                for t in range(self.columns):
                    if self.board[t][i] == 'R':
                        rstreak = rstreak + 1
                    else:
                        rstreak = 0
                if (rstreak == 4):
                    print("Red row win")
                    return True

        return False

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
