import random


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
        print("Rules of Tic Tac Toe: You play as either X or O on an 3 by 3 board 2) \
        to win, you must create a diagonal, horizontal, or vertical line of 3 3) the game ends when all 9 boxes are filled. ")
        return

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
        if(player == 0):
            self.board[row][col] = 'X'

        if (player == 1):
            self.board[row][col] = 'O'

    def take_manual_turn(self, player):

        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        Valid = False
        while Valid == False:
            print("please enter a valid move")
            row = input("what row do you want to play")
            col = input("what column do you want to play")
            if self.is_valid_move(row, col):
                Valid = True
        self.place_player(player,row, col)

    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
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
            for i in range(self.columns):
                if(self.board[i][t] == '-'):
                    allEmpty = False
        if (allEmpty == True):
            return True

        return False

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
                self.take_turn(1)
                print("player 2 turn")
            self.print_board()

        if (self.check_win(0) == True):
            self.print_board()
            print("X wins!")


        elif (self.check_win(1) == True):
            self.print_board()
            print("O wins!")

    def take_random_turn(self, player):
        randX = random.randrange(3)
        randY = random.randrange(3)
        keeptrying = True
        while keeptrying==True:
            print("random col = " + str(randX))
            print("random row = " + str(randY))
            if (self.is_valid_move(player, randX, randY) == True):
                keeptrying = False;
                self.place_player(player, randX, randY)
