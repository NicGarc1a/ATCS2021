import random
import math
import sys



class ConnectFour:
    def __init__(self):
        self.board = []
        self.columns = 8
        self.rows = 8
        self.boardcopy = []

        for i in range(self.columns):
            row = []
            for t in range(self.rows):
                dash = "-"
                row.append(dash.strip())
            self.board.append(row)
            self.boardcopy.append(row)

    def print_instructions(self):
        print("Rules of Connect Four: You can play another player or an AI on an 8X8 board")
        print("2)  to win, you must create a diagonal, horizontal, or vertical line of 4")
        print("3) the game ends when either player wins")
        print("")

    def print_board(self):
        print("   0 1 2 3 4 5 6 7")
        for t in range(self.columns):
            print(str(t), end='  ')
            print(*self.board[t])


    def is_valid_move(self, row, col):
        if (self.board[row][col] == '-'):
            return True
        return False

    def place_player(self, board1, player, row, col):

        if (player == 0):
            board1[row][col] = 'B'

        if (player == 1):
            board1[row][col] = 'R'

        if (player == '-'):
            board1[row][col] = '-'

    def take_manual_turn(self, player):

        while (True):
            try:
                full = True
                while(full == True):
                    colInput = int(input("What column to drop: "))
                    if (self.board[0][colInput] != '-'):
                        print("That column is full go again")
                    else:
                        full = False
                for i in range(8):
                    if (self.board[7][colInput] == '-'):
                        rowInput = 7
                    elif (self.board[i][colInput] == '-'):
                        rowInput = i
                if (player == 0):
                    self.place_player(self.board, 0, rowInput, colInput)
                elif (player == 1):
                    self.place_player(self.board,1, rowInput, colInput)

            except IndexError:
                print("this is not a valid response")
                continue
            except ValueError:
                print("this is not a valid response")
                continue
            return


    def take_turn(self, player):
        if player ==0:
            print()
            print("Player 1 (Blue), take your turn:")
            self.take_manual_turn(player)
        elif player == 1:
            print()
            print("Player 2 (Red), take your turn:")
            self.take_manual_turn(player)


    def check_col_win(self, player):
        bstreak = 0
        rstreak = 0
        if (player == 0):
            for i in range(self.columns):
                bstreak = 0
                for t in range(self.columns):
                    if self.board[t][i] == 'B':
                        bstreak = bstreak + 1
                    else:
                        bstreak = 0
                if (bstreak == 4):
                    return True
        if (player == 1):
            for i in range(self.columns):
                rstreak = 0
                for t in range(self.columns):
                    if self.board[t][i] == 'R':
                        rstreak = rstreak + 1
                    else:
                        rstreak = 0
                if (rstreak == 4):
                    return True

        return False

    def check_row_win(self, player):
        bstreak = 0
        rstreak = 0
        if (player == 0):
            for i in range(self.columns):
                bstreak = 0
                for t in range(self.columns):
                    if self.board[i][t] == 'B':
                        bstreak = bstreak + 1
                    else:
                        bstreak = 0
                if (bstreak == 4):
                    return True
        if (player == 1):
            for i in range(self.columns):
                rstreak = 0
                for t in range(self.columns):
                    if self.board[i][t] == 'R':
                        rstreak = rstreak + 1
                    else:
                        rstreak = 0
                if (rstreak == 4):
                    return True

        return False

    def check_diag_win(self, player):

        if (player == 0):
            for col1 in range(3,8):
                startcol = col1
                startrow= 0
                bstreak = 0
                while startcol != -1:
                    if self.board[startrow][startcol] == 'B':
                        bstreak = bstreak +1
                    else:
                        bstreak = 0
                    if bstreak == 4:
                        return True
                    startrow = startrow + 1
                    startcol = startcol -1
            for row1 in range(1,5):
                startcol = 7
                startrow = row1
                bstreak = 0
                while startrow != 8:
                    if self.board[startrow][startcol] == 'B':
                        bstreak = bstreak +1
                    else:
                        bstreak = 0
                    if bstreak == 4:
                        return True
                    startrow = startrow + 1
                    startcol = startcol -1
            for col1 in range(3,8):
                startcol = col1
                startrow = 7
                bstreak = 0
                while startcol != -1:
                    if self.board[startrow][startcol] == 'B':
                        bstreak = bstreak +1
                    else:
                        bstreak = 0
                    if bstreak == 4:
                        return True
                    startrow = startrow - 1
                    startcol = startcol - 1
            for row1 in range(3,7):
                startcol = 7
                startrow = row1
                bstreak = 0
                while startrow != -1:
                    if self.board[startrow][startcol] == 'B':
                        bstreak = bstreak +1
                    else:
                        bstreak = 0
                    if bstreak == 4:
                        return True
                    startrow = startrow - 1
                    startcol = startcol - 1
        elif (player == 1):
            for col1 in range(3,8):
                startcol = col1
                startrow= 0
                bstreak = 0
                while startcol != -1:
                    if self.board[startrow][startcol] == 'R':
                        bstreak = bstreak +1
                    else:
                        bstreak = 0
                    if bstreak == 4:
                        return True
                    startrow = startrow + 1
                    startcol = startcol -1
            for row1 in range(1,5):
                startcol = 7
                startrow = row1
                bstreak = 0
                while startrow != 8:
                    if self.board[startrow][startcol] == 'R':
                        bstreak = bstreak +1
                    else:
                        bstreak = 0
                    if bstreak == 4:
                        return True
                    startrow = startrow + 1
                    startcol = startcol -1
            for col1 in range(3,8):
                startcol = col1
                startrow = 7
                bstreak = 0
                while startcol != -1:
                    if self.board[startrow][startcol] == 'R':
                        bstreak = bstreak +1
                    else:
                        bstreak = 0
                    if bstreak == 4:
                        return True
                    startrow = startrow - 1
                    startcol = startcol - 1
            for row1 in range(3,7):
                startcol = 7
                startrow = row1
                bstreak = 0
                while startrow != -1:
                    if self.board[startrow][startcol] == 'R':
                        bstreak = bstreak +1
                    else:
                        bstreak = 0
                    if bstreak == 4:
                        return True
                    startrow = startrow - 1
                    startcol = startcol - 1

    def check_win(self, player):
        # TODO: Check win

        if(self.check_col_win(player) == True or self.check_row_win(player) == True or self.check_diag_win(player) == True):
            return True
        else:
            return False


    def check_tie(self):
        nomoves = True
        for i in range(self.columns):
            for t in range(self.columns):
                if (self.board[i][t] == '-'):
                    nomoves = False
        if (nomoves == True):
            return True
        return False

    def minimax2(self, board1, player, depth, alpha, beta):
        if(player == 1):
            max = -1000000
            column = random.randint(0, 8)
            row = 0
            rowInput = 0
            for t in range(8):
                for i in range(8):
                    if (self.board[7][t] == '-'):
                        rowInput = 7
                    elif (self.board[i][t] == '-'):
                        rowInput = i
                if (self.is_valid_move(rowInput, t)):
                    boardcopy = board1.copy()
                    self.place_player(boardcopy, 0, rowInput, t)
                    score = self.minimax2(boardcopy, 0, depth - 1, alpha, beta)[0]
                    if score > max:
                        max = score
                        column = t
                        row = rowInput
                    if alpha > max:
                        alpha = alpha
                    else:
                        alpha = max
                    if alpha >= beta:
                        break
            return (max, row, column)
        else:
            min = 100000
            column = random.randint(0,8)
            row = 0
            rowInput = 0
            for t in range(8):
                for i in range(8):
                    if (self.board[7][t] == '-'):
                        rowInput = 7
                    elif (self.board[i][t] == '-'):
                        rowInput = i
                if (self.is_valid_move(rowInput, t)):
                    boardcopy = board1.copy()
                    self.place_player(boardcopy, 1, rowInput, t)
                    score = self.minimax2(boardcopy, 1, depth - 1, alpha, beta)[0]
                    if score < min:
                        min = score
                        row = rowInput
                        column = t
                    if beta < min:
                        beta = beta
                    else:
                        beta = min
                    if alpha>= beta:
                        break
            return (min, row, column)

    # def minimax(self, player, depth):
    #
    #     if self.check_win(1):
    #         return (10, None, None)
    #     if self.check_win(0):
    #         return (-10, None, None)
    #     if self.check_tie():
    #         return (0, None, None)
    #     if (depth == 0):
    #         return (0, None, None)
    #
    #
    #     if (player == 1):
    #         max = -100
    #         row = -1
    #         col = -1
    #         rowInput = 0
    #
    #         for t in range(8):
    #             for i in range(8):
    #                 if (self.board[7][t] == '-'):
    #                     rowInput = 7
    #                 elif (self.board[i][t] == '-'):
    #                     rowInput = i
    #             if (self.is_valid_move(rowInput, t)):
    #                 self.place_player(1, rowInput,t)
    #                 score = -10
    #                 score = self.minimax(0, depth - 1)[0]
    #                 if (max < score):
    #                     max = score
    #                     row = rowInput
    #                     col = t
    #                 self.place_player("-", rowInput, t)
    #         return (max, row, col)
    #     if (player == 0):
    #         min = 100
    #         row = -1
    #         col = -1
    #
    #         for t in range(8):
    #             for i in range(8):
    #                 if (self.board[7][t] == '-'):
    #                     rowInput = 7
    #                 elif (self.board[i][t] == '-'):
    #                     rowInput = i
    #             if (self.is_valid_move(rowInput, t)):
    #                 self.place_player(0, rowInput,t)
    #                 score = 10
    #                 score = self.minimax(1, depth - 1)[0]
    #                 if (min > score):
    #                     min = score
    #                     row = rowInput
    #                     col = t
    #                 self.place_player("-", rowInput, t)
    #         return (min, row, col)
    #
    #

    def take_minimax_turn(self, player, depth):
        score, row, col = self.minimax2(self.board,player, depth, -100000, 100000)
        print("row is " + str(row))
        print("col is " + str(col))
        if self.is_valid_move(row, col):
            self.place_player(player, row, col)

        else:
            print("invalid")

    def play_game(self):
        playerTurn = 0
        self.print_instructions()
        gamemode = int(input("What game mode would you like to play (1 for  minimax, 2 for  multiplayer) "))

        self.print_board()

        if (gamemode == 1):

            while (self.check_win(0) != True and self.check_win(1) != True):
                playerTurn += 1
                if (playerTurn % 2 == 1):
                    self.take_turn(0)
                    print("player 1 turn (Blue)")
                elif (playerTurn % 2 == 0):
                    self.take_minimax_turn(1, 5)
                    print("player 2 turn (Red)")
                self.print_board()
                if (self.check_tie()):
                    print("tie")
                    break

            if (self.check_win(0) == True):
                self.print_board()
                print("Blue wins!")


            elif (self.check_win(1) == True):
                self.print_board()
                print("Red Minimax AI wins!")

        elif(gamemode == 2):
            while (self.check_win(0) != True and self.check_win(1) != True):
                playerTurn += 1
                if (playerTurn % 2 == 1):
                    self.take_turn(0)
                    print("player 1 turn (Blue)")
                elif (playerTurn % 2 == 0):
                    self.take_turn(1)
                    print("player 2 turn (Red)")
                self.print_board()
                if (self.check_tie()):
                    print("tie")
                    break

            if (self.check_win(0) == True):
                self.print_board()
                print("Blue wins!")


            elif (self.check_win(1) == True):
                self.print_board()
                print("Red wins!")


