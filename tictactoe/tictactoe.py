import random
import time

class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = []
        self.columns = 3
        self.rows = 3

        for i in range(self.columns):
            row = []
            for t in range(self.rows):
                dash = "-"
                row.append(dash.strip())
            self.board.append(row)

    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("Rules of Tic Tac Toe: You play as either X or O on an 3 by 3 board")
        print("2)  to win, you must create a diagonal, horizontal, or vertical line of 3")
        print("3) the game ends when all 9 boxes are filled.")

    def print_board(self):
        # TODO: Print the board
        print("   0 1 2")
        for t in range(self.columns):
            print(str(t), end='  ')
            print(*self.board[t])

    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        if (self.board[row][col] == '-'):
            return True
        return False

    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        if (player == 0):
            self.board[row][col] = 'X'

        if (player == 1):
            self.board[row][col] = 'O'
        if (player == '-'):
            self.board[row][col] = '-'

    def take_manual_turn(self, player):

        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        while (True):
            try:
                rowInput = int(input("What row to place: "))
                colInput = int(input("What column to place: "))
                if (self.is_valid_move(rowInput, colInput)):
                    if (player == 0):
                        self.place_player(0, rowInput, colInput)
                    elif (player == 1):
                        self.place_player(1, rowInput, colInput)
                else:
                    # manually throwing an error if space isnt empty, i know its lazy, im sorry
                    self.board[100][100] == '-'
            except IndexError:
                print("this is not a valid response")
                continue
            except ValueError:
                print("this is not a valid response")
                continue
            return

    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        print()
        print("Player 1, take your turn:")
        self.take_manual_turn(player)

    def check_col_win(self, player):
        # TODO: Check col win
        if (player == 0):
            for i in range(self.columns):
                winCondition = True
                for t in range(self.columns):
                    if self.board[t][i] != 'X':
                        winCondition = False
                if (winCondition == True):
                    print("col win")
                    return True
        if (player == 1):
            for i in range(self.columns):
                winCondition = True
                for t in range(self.columns):
                    if self.board[t][i] != 'O':
                        winCondition = False
                if (winCondition == True):
                    print("col win")
                    return True

        return False

    def check_row_win(self, player):
        # TODO: Check row win
        if (player == 0):
            for i in range(self.columns):
                winCondition = True
                for t in range(self.columns):
                    if self.board[i][t] != 'X':
                        winCondition = False
                if (winCondition == True):
                    print("row win")
                    return True
        if (player == 1):
            for i in range(self.columns):
                winCondition = True
                for t in range(self.columns):
                    if self.board[i][t] != 'O':
                        winCondition = False
                if (winCondition == True):
                    print("row win")
                    return True

        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        if (player == 0):
            winCondition = True
            for i in range(self.columns):
                if (self.board[i][i] != 'X'):
                    winCondition = False
            if (winCondition == True):
                return True
            elif(self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X'):
                return True

        elif (player == 1):
            winCondition = True
            for i in range(self.columns):
                if (self.board[i][i] != 'O'):
                    winCondition = False
            if(winCondition == True):
                return True
            elif (self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X'):
                return True
        return False

    def check_win(self, player):
        # TODO: Check win

        if(self.check_col_win(player) == True or self.check_row_win(player) == True or self.check_diag_win(player) == True):
            return True
        else:
            return False


    def check_tie(self):
        # TODO: Check tie
        allEmpty = True
        for i in range(self.columns):
            for t in range(self.columns):
                if (self.board[i][t] == '-'):
                    allEmpty = False
        if (allEmpty == True):
            return True

        return False

    def minimax(self, player, depth):

        if self.check_win(1):
            return (10, None, None)
        if self.check_win(0):
            return (-10, None, None)
        if self.check_tie():
            return (0, None, None)
        if (depth == 0):
            return (0, None, None)


        if (player == 1):
            max = -10
            row = -1
            col = -1
            for i in range(self.columns):
                for t in range(self.rows):
                    if (self.is_valid_move(i, t)):
                        self.place_player(1, i, t)
                        score = -10
                        score = self.minimax(0, depth - 1)[0]
                        if (max < score):
                            max = score
                            row = i
                            col = t
                        self.place_player("-", i, t)
            return (max, row, col)
        if (player == 0):
            min = 10
            row = -1
            col = -1
            for i in range(self.columns):
                for t in range(self.rows):
                    if (self.is_valid_move(i, t)):
                        self.place_player(0, i, t)
                        score = 10
                        score = self.minimax(1, depth - 1)[0]
                        if (min > score):
                            min = score
                            row = i
                            col = t
                        self.place_player("-", i, t)
            return (min, row, col)

    def take_minimax_turn(self, player, depth):
        score, row, col = self.minimax(player, depth)
        print("row is " + str(row))
        print("col is " + str(col))
        if self.is_valid_move(row, col):
            self.place_player(player, row, col)

        else:
            print("invalid")

    def play_game(self):
        # TODO: Play game
        # TODO: Play game
        playerTurn = 0
        self.print_instructions()
        self.print_board()

        while (self.check_win(0) != True and self.check_win(1) != True):
            playerTurn += 1
            if (playerTurn % 2 == 1):
                self.take_turn(0)
                print("player 1 turn")
            elif (playerTurn % 2 == 0):
                self.take_minimax_turn(1, 4)
                print("player 2 turn")
            self.print_board()
            if (self.check_tie()):
                print("tie")
                break

        if (self.check_win(0) == True):
            self.print_board()
            print("X wins!")


        elif (self.check_win(1) == True):
            self.print_board()
            print("O wins!")