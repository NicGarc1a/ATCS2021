import random
import sys
import pygame


class ConnectFour:
    def __init__(self):
        # initialize an 8*8 board array
        self.board = []
        self.columns = 8
        self.rows = 8

        # fill the array with empty spaces (-)
        for i in range(self.columns):
            row = []
            for t in range(self.rows):
                dash = "-"
                row.append(dash.strip())
            self.board.append(row)

    # print instructions of connect four (TO DO: make a GUI version of this)
    def print_instructions(self):
        print("Rules of Connect Four: You can play another player or an AI on an 8X8 board")
        print("2)  to win, you must create a diagonal, horizontal, or vertical line of 4")
        print("3) the game ends when either player wins")
        print("")
    # print board for console using for loop (number the rows and columns)
    def print_board(self):
        print("   0 1 2 3 4 5 6 7")
        for t in range(self.columns):
            print(str(t), end='  ')
            print(*self.board[t])

    # checks if a potential move is valid ( if the space is empty)
    def is_valid_move(self, row, col):
        if (self.board[row][col] == '-'):
            return True
        return False
    # takes in the players position and alters the array to reflect that
    def place_player(self, player, row, col):

        if (player == 0):
            self.board[row][col] = 'B'

        if (player == 1):
            self.board[row][col] = 'R'

        if (player == '-'): # for when Ai needs to temporarily fill a square and then re empty it
            self.board[row][col] = '-'

    # for non AI player
    def take_manual_turn(self, player, colInput):

        while (True):
            try:# avoid errors
                full = True
                for i in range(8): # for loop takes in the column input and finds the lowest available row for that column
                    if (self.board[7][colInput] == '-'):
                        rowInput = 7
                    elif (self.board[i][colInput] == '-'):
                        rowInput = i
                if (player == 0): # changes the array with the players input ( col) and for loop result (row)
                    self.place_player(0, rowInput, colInput)
                elif (player == 1):
                    self.place_player(1, rowInput, colInput)

            except IndexError: # avoid errors
                print("this is not a valid response")
                continue
            except ValueError:
                print("this is not a valid response")
                continue
            return

    # takes in key strokes from each player
    def take_turn(self, player):
        inputtime = True
        if player ==0: # Blue Player
            print()
            print("Player 1 (Blue), take your turn:")
            while (inputtime == True):  # uses the pygame event function to take in keystrokes while on the GUI
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_0:
                            colInput = 0
                            inputtime = False
                        if event.key == pygame.K_1:
                            colInput = 1
                            inputtime = False
                        if event.key == pygame.K_2:
                            colInput = 2
                            inputtime = False
                        if event.key == pygame.K_3:
                            colInput = 3
                            inputtime = False
                        if event.key == pygame.K_4:
                            colInput = 4
                            inputtime = False
                        if event.key == pygame.K_5:
                            colInput = 5
                            inputtime = False
                        if event.key == pygame.K_6:
                            colInput = 6
                            inputtime = False
                        if event.key == pygame.K_7:
                            colInput = 7
                            inputtime = False
            self.take_manual_turn(player, colInput)
        elif player == 1: # same thing as above but for Red in the case of Player V player
            print()
            print("Player 2 (Red), take your turn:")
            while (inputtime == True):
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            colInput = 1
                            inputtime = False
                        if event.key == pygame.K_2:
                            colInput = 2
                            inputtime = False
                        if event.key == pygame.K_RETURN:
                            colInput = 3
                            input = False
                        if event.key == pygame.K_4:
                            colInput = 4
                            inputtime = False
                        if event.key == pygame.K_5:
                            colInput = 5
                            inputtime = False
                        if event.key == pygame.K_6:
                            colInput = 6
                            input = False
                        if event.key == pygame.K_7:
                            colInput = 6
                            input = False
            self.take_manual_turn(player, colInput)

    # checks for a column streak
    def check_col_win(self, player):
        bstreak = 0
        rstreak = 0
        if (player == 0):
            for i in range(self.columns):
                bstreak = 0 #restarts the streak counter at each new column so that wrong wins arent counted
                for t in range(self.columns): # goes from 0 to 7 counting the streak
                    if self.board[t][i] == 'B':
                        bstreak = bstreak + 1
                    else: # resets if there is a non B piece
                        bstreak = 0
                    if (bstreak == 4):
                        return True
        if (player == 1): # same thing as above but for player 1 (red)
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
    # checks for a row win for the player input
    def check_row_win(self, player):
        bstreak = 0
        rstreak = 0
        if (player == 0):
            for i in range(8):
                bstreak = 0 # restarts the streak at the start of every row
                for t in range(8):
                    if self.board[i][t] == 'B':
                        bstreak = bstreak + 1
                    else:
                        bstreak = 0
                    if (bstreak == 4):
                        return True
        if (player == 1):
            for i in range(self.columns):
                rstreak = 0# restarts the streak at the start of every row
                for t in range(self.columns):
                    if self.board[i][t] == 'R':
                        rstreak = rstreak + 1
                    else:
                        rstreak = 0
                    if (rstreak == 4):
                        return True

        return False
    # check diagonal wins
    def check_diag_win(self, player):

        if (player == 0):
            for col1 in range(3,8): # goes from the points 03,04,05,06,07 and goes up diagonally checking for streak of 4
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
            for row1 in range(1,5): # goes from the points 17, 27, 37, 47 and goes up diagonally checking for streak of 4
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
            for col1 in range(3,8): # goes from the points 73,74,75,76,77  and goes down diagonally checking for streak of 4
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
            for row1 in range(3,7): # goes from the points 67, 57, 47, 37 and goes down diagonally checking for streak of 4
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
        elif (player == 1): # same thing as above but for player Red
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
        # checks all of the check win methods to see if a player has win diagonally, vertically, horizontally
        if(self.check_col_win(player) == True or self.check_row_win(player) == True or self.check_diag_win(player) == True):
            return True
        else:
            return False

    # checks if the board is full ajnd because the win checker has not been triggered there is a tie
    def check_tie(self):
        nomoves = True
        for i in range(self.columns):
            for t in range(self.columns):
                if (self.board[i][t] == '-'):
                    nomoves = False
        if (nomoves == True):
            return True
        return False

    def statemachine(self, player):
        rowInput = 0
        # STATE: OFFENSE (if there is a winnable move it will be played)
        for col in range(8):
            for i in range(8):
                if (self.board[7][col] == '-'):
                    rowInput = 7
                elif (self.board[i][col] == '-'):
                    rowInput = i
            if (self.is_valid_move(rowInput, col)):
                self.place_player(player, rowInput, col)
                if (self.check_win(player)):
                    self.place_player('-', rowInput, col)
                    return (rowInput, col)
                self.place_player('-', rowInput, col)
        # STATE: DEFENSE (if there is a winnable move for the other player it will be played)
        for col in range(8):
            for i in range(8):
                if (self.board[7][col] == '-'):
                    rowInput = 7
                elif (self.board[i][col] == '-'):
                    rowInput = i
            if (self.is_valid_move(rowInput, col)):
                self.place_player(0, rowInput, col)
                if (self.check_win(0)):
                    self.place_player('-', rowInput, col)
                    return (rowInput, col)
                self.place_player('-', rowInput, col)
         # STATE : FIRST MOVe : will play a piece to the left of first player

        bottomemptystreak = 0
        opponentfirstmovecol = 0
        for i in range(8):
            if (self.board[7][i] == '-'):
                bottomemptystreak = bottomemptystreak + 1
            else:
                opponentfirstmovecol = i

        if bottomemptystreak ==7:
            return (7, opponentfirstmovecol-1)

        # STATE: STREAKMAKER (if no one will win in 1 move, the AI will place wherever will have the most immediately connected pieces)
        recordstreak = 0
        streakrow = 0
        streakcol = 0

        for col in range(8):
            streak = 0

            for i in range(8):
                if (self.board[7][col] == '-'):
                    rowInput = 7
                elif (self.board[i][col] == '-'):
                    rowInput = i
            # check the diagonal streak of a point
            if (rowInput!= 0 and col != 7 ):
                if (self.board[rowInput-1][col+1] == 'R'):
                    streak = streak + 1
            if (rowInput!= 7 and col != 0 ):
                if (self.board[rowInput+1][col-1] == 'R'):
                    streak = streak + 1
            # check the horizontal streak of a point
            if (col!= 7):
                if (self.board[rowInput][col+1] == 'R'):
                    streak = streak + 1
            if (col !=0):
                if (self.board[rowInput][col-1] == 'R'):
                    streak = streak + 1


            # check the vertical streak of a point
            if (rowInput!= 7):
                if (self.board[rowInput+1][col] == 'R'):
                    streak = streak + 1

            if streak >= recordstreak:
                recordstreak = streak
                streakrow = rowInput
                streakcol = col
        return (streakrow, streakcol)





# gets the coords from the statemachine method and checks if it is valid and places it on the board
    def take_statemachine_turn(self, player):
        row, col = self.statemachine(player)
        print("row is " + str(row))
        print("col is " + str(col))
        if self.is_valid_move(row, col):
            self.place_player(player, row, col)

        else:
            print("invalid")

#
    def minimax(self, player, depth, alpha, beta):
        rowInput = 0
        # makes sure the move isnt terminal
        if self.check_win(1):
            return (10, None, None)
        if self.check_win(0):
            return (-10, None, None)
        if self.check_tie():
            return (0, None, None)
        if (depth == 0):
            return (0, None, None)

        # the max section of the minimax algorithm  (MAXIMIZES THE score of AI)
        if (player == 1):
            maximum = -100 # start the mas at a very low value
            row = -1
            col = -1

            for t in range(self.rows):
                for i in range(8):
                    if (self.board[7][t] == '-'):
                        rowInput = 7
                    elif (self.board[i][t] == '-'):
                        rowInput = i
                if (self.is_valid_move(rowInput, t)):
                    self.place_player(1, rowInput,t)
                    score = self.minimax(0, depth - 1, alpha, beta)[0]
                    alpha = max(alpha, score)
                    if (maximum < score):
                        maximum = score
                        row = rowInput
                        col = t
                    self.place_player("-", rowInput, t)
                    if (alpha >= beta):
                        return (maximum, row, col)
            return (maximum, row, col)
        if (player == 0): # minimizes the score of the real player
            minimum = 100 # start the minimum value low
            row = -1
            col = -1

            for t in range(self.rows): # finds the columns corresponding row
                for i in range(8):
                    if (self.board[7][t] == '-'):
                        rowInput = 7
                    elif (self.board[i][t] == '-'):
                        rowInput = i
                if (self.is_valid_move(rowInput, t)):
                    self.place_player(0, rowInput,t)
                    score = self.minimax(1, depth - 1, alpha, beta)[0]
                    beta = min(beta, score)
                    if (minimum > score):
                        minimum = score
                        row = rowInput
                        col = t
                    self.place_player("-", rowInput, t)
                    if (alpha >= beta):
                       return (minimum, row, col)
            return (minimum, row, col)

    # gets the coords from the minimax method and checks if it is valid and places it on the board
    def take_minimax_turn(self, player, depth, alpha, beta):
        score, row, col = self.minimax(player, depth, alpha, beta)
        print("row is " + str(row))
        print("col is " + str(col))
        if self.is_valid_move(row, col):
            self.place_player(player, row, col)

        else:
            print("invalid")
    # uses the pygame library to create a square (500 by 500) for the GUI and fill it with images i designed in illustrator
    # based on the state of the game
    def draw_board(self, state,display):
        pygame.display.update() # not necessary but makes sure there are no display lagging mistakes
        if (state == "welcome"): #the welcome page that the player has to press enter to leave
            welcomeimage = pygame.image.load("Welcome.png").convert()
            welcomeimage =pygame.transform.smoothscale(welcomeimage, (500,500))
            display.blit(welcomeimage, (0,0))
            pygame.display.update()

        if(state == "game"): #prints the board ( an image i designed in illustrator) and prints the red and blue pieces
            boardimage = pygame.image.load("game.png").convert()
            boardimage =pygame.transform.smoothscale(boardimage, (500,500))
            display.blit(boardimage, (0,0))
            for col in range(self.columns):
                xcoord = 16 + (col*60) # 16 is space between the left edge and the first column ( 60 is the space between the left corners of the tokens)
                for row in range(self.rows):
                    ycoord = 43 + (row*56) #43 is space between the top edge and the first row ( 56 is the space between the left corners of the tokens)
                    if(self.board[row][col]=="R"):
                        redpiece = pygame.image.load("redpiece.png")
                        redpiece = pygame.transform.smoothscale(redpiece, (47, 47))
                        display.blit(redpiece, (xcoord, ycoord))

                    elif (self.board[row][col] == "B"):
                        bluepiece = pygame.image.load("bluetoken.png")
                        bluepiece = pygame.transform.smoothscale(bluepiece, (47, 47))
                        display.blit(bluepiece, (xcoord, ycoord))
            pygame.display.update()

        elif (state == "menu"): # prints the menu page which shoiws the game modes
            menuimage = pygame.image.load("Menu.png").convert()
            menuimage = pygame.transform.smoothscale(menuimage, (500, 500)) # smooth scale makes the resizing not affect quality
            display.blit(menuimage, (0, 0))
            pygame.display.update()


        elif (state == "redwin"): # the win page if red wins
            redwinimage = pygame.image.load("redwin.png").convert()
            redwinimage = pygame.transform.smoothscale(redwinimage, (500, 500))
            display.blit(redwinimage, (0, 0))
            pygame.display.update()

        elif (state == "bluewin"): # the win page for blue win
            bluewinimage = pygame.image.load("bluewin.png").convert()
            bluewinimage = pygame.transform.smoothscale(bluewinimage, (500, 500))
            display.blit(bluewinimage, (0, 0))
            pygame.display.update()


    def play_game(self):
        pygame.display.init()
        display = pygame.display.set_mode((500,500)) #makes a 500 by 500  display
        playerTurn = 0
        self.print_instructions()
        self.draw_board("welcome",display)
        welcome = 0
        while welcome != 2:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome =2
                        break

        self.draw_board("menu",display)
        gamemode = 0
        while gamemode == 0:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        gamemode = 1
                        break
                    if event.key == pygame.K_2:
                        gamemode = 2
                        break
                    if event.key == pygame.K_3:
                        gamemode = 3
                        break
        self.draw_board("game",display)
        self.print_board()
        redwin = False
        bluewin = False

        if (gamemode == 3):# player vs minimax

            while (self.check_win(0) != True and self.check_win(1) != True):
                playerTurn += 1
                if (playerTurn % 2 == 1):
                    self.take_turn(0)
                    print("player 1 turn (Blue)")
                elif (playerTurn % 2 == 0):
                    self.take_minimax_turn(1, 5, -1000, 1000)
                    print("player 2 turn (Red)")
                self.print_board()
                self.draw_board("game", display)
                if (self.check_tie()):
                    print("tie")
                    break

            if (self.check_win(0) == True):
                self.draw_board("bluewin", display)
                self.print_board()
                print("Blue wins!")
                bluewin = True



            elif (self.check_win(1) == True):
                self.draw_board("redwin", display)
                self.print_board()
                print("Red Minimax AI wins!")
                redwin = True


        elif(gamemode == 2): # player vs player
            while (self.check_win(0) != True and self.check_win(1) != True):
                playerTurn += 1
                if (playerTurn % 2 == 1):
                    self.take_turn(0)
                    print("player 1 turn (Blue)")
                elif (playerTurn % 2 == 0):
                    self.take_turn(1)
                    print("player 2 turn (Red)")
                self.print_board()
                self.draw_board("game",display)
                if (self.check_tie()):
                    print("tie")
                    break

            if (self.check_win(0) == True):
                self.print_board()
                self.draw_board("bluewin",display)

                print("Blue wins!")
                bluewin = True



            elif (self.check_win(1) == True):
                self.print_board()
                self.draw_board("redwin",display)
                print("Red wins!")
                redwin = True

        elif(gamemode == 1): # player vs statemachine
            while (self.check_win(0) != True and self.check_win(1) != True):
                playerTurn += 1
                if (playerTurn % 2 == 1):
                    self.take_turn(0)
                    print("player 1 turn (Blue)")
                elif (playerTurn % 2 == 0):
                    self.take_statemachine_turn(1)
                    print("player 2 turn (Red)")
                self.print_board()
                self.draw_board("game",display)
                if (self.check_tie()):
                    print("tie")
                    break

            if (self.check_win(0) == True):
                self.print_board()
                self.draw_board("bluewin",display)
                print("Blue wins!")
                bluewin = True




            elif (self.check_win(1) == True):
                self.print_board()
                self.draw_board("redwin",display)
                print("Red wins!")
                redwin = True
        while (bluewin == True):
            self.draw_board("bluewin", display)
        while (redwin == True):
            self.draw_board("redwin", display)
