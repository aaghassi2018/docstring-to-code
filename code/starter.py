# Hw 10, pr2 for CS 5 gold, 2016
#
# The Board class from CS 5 Hw #10
# for use as a starting point for
# Hw#11, the Player class (and AI)
#
import random

class Board:
    """A datatype representing a C4 board
       with an arbitrary number of rows and cols.
    """

    def __init__(self, width = 7, height = 6):
        """The constructor for objects of type Board."""
        self.width = width
        self.height = height
        self.data = [[' '] * width for r in range(height)]

        # do not need to return inside a constructor!


    def __repr2__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''         # the string to return
        for row in range(self.height):
            s += '|'   # add the spacer character
            for col in range(self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += '-' * (self.width * 2) + '-\n'
        for col in range(self.width):
            s += ' ' + str(col % 10)


        return s





    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''         # the string to return
        for row in range(self.height):
            s += '|'   # add the spacer character
            for col in range(self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += '--' * self.width # add the bottom of the board
        s += '-\n'

        for col in range(self.width):
            s += ' ' + str(col%10)

        s += '\n'
        return s       # the board is complete, return it

    def set_board(self, LoS):
        """This method returns a string representation
           for an object of type Board.
        """
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = LoS[row][col]

    def setBoard(self, moves, show = True):
        """Sets the board according to a string
           of turns (moves), starting with 'X'.
           If show == True, it prints each one.
        """
        nextCh = 'X'
        for move in moves:
            col = int(move)
            if self.allowsMove(col):
                self.addMove(col, nextCh)
            if nextCh == 'X':
                nextCh = 'O'
            else:
                nextCh = 'X'
            if show:
                print(self)

    def set(self, moves, show = True):
        """Sets the board according to a string
           of turns (moves), starting with 'X'.
           If show==True, it prints each one.
        """
        nextCh = 'X'
        for move in moves:
            col = int(move)
            if self.allowsMove(col):
                self.addMove(col, nextCh)
            if nextCh == 'X':
                nextCh = 'O'
            else:
                nextCh = 'X'
            if show:
                print(self)

    def clear(self):
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = ' '

    def addMove(self, col, ox):
        """Adds checker ox into column col.
           Does not need to check for validity;
           allowsMove will do that.
        """
        row = self.height - 1
        while row >= 0:
            if self.data[row][col] == ' ':
                self.data[row][col] = ox
                return
            row -= 1


    def addMove2(self, col, ox):
        """Adds checker ox into column col.
           Does not need to check for validity;
           allowsMove will do that.
        """
        for row in range(self.height):
            # look for the first nonempty row
            if self.data[row][col] != ' ':
                # put in the checker
                self.data[row-1][col] = ox
                return
        self.data[self.height-1][col] = ox

    def delMove(self, col):
        """Removes the checker from column col."""
        for row in range(self.height):
            # look for the first nonempty row
            if self.data[row][col] != ' ':
                # put in the checker
                self.data[row][col] = ' '
                return
        # it's empty, just return
        return


    def allowsMove(self, col):
        """Returns True if a move to col is allowed
           in the board represented by self;
           returns False otherwise
        """
        if col < 0 or col >= self.width:
            return False
        return self.data[0][col] == ' '

    def isFull(self):
        """Returns True if the board is completely full."""
        for col in range(self.width):
            if self.allowsMove(col):
                return False
        return True

    def gameOver(self):
        """Returns True if the game is over."""
        if self.isFull() or self.winsFor('X') or self.winsFor('O'):
            return True
        return False

    def isOX(self, row, col, ox):
        """Checks if the spot at row, col is legal and ox."""
        if 0 <= row < self.height:
            if 0 <= col < self.width: # legal...
                if self.data[row][col] == ox:
                    return True
        return False

    def winsFor(self, ox):
        """Checks if the board self is a win for ox."""
        for row in range(self.height):
            for col in range(self.width):
                if self.isOX(row, col, ox) and \
                   self.isOX(row+1, col, ox) and \
                   self.isOX(row+2, col, ox) and \
                   self.isOX(row+3, col, ox):
                    return True
                if self.isOX(row, col, ox) and \
                   self.isOX(row, col+1, ox) and \
                   self.isOX(row, col+2, ox) and \
                   self.isOX(row, col+3, ox):
                    return True
                if self.isOX(row, col, ox) and \
                   self.isOX(row+1, col+1, ox) and \
                   self.isOX(row+2, col+2, ox) and \
                   self.isOX(row+3, col+3, ox):
                    return True
                if self.isOX(row, col, ox) and \
                   self.isOX(row+1, col-1, ox) and \
                   self.isOX(row+2, col-2, ox) and \
                   self.isOX(row+3, col-3, ox):
                    return True
        return False

# Here is a version of hostGame for use in your Board class
#
# it simply alternates moves in the game and checks if
# the game is over at each move


    def hostGame(self):
        """Hosts a game of Connect Four."""

        nextCheckerToMove = 'X'

        while True:
            # print the board
            print(self)

            # get the next move from the human player...
            col = -1
            while not self.allowsMove(col):
                col = int(input('Next col for ' + nextCheckerToMove + ': '))
            self.addMove(col, nextCheckerToMove)

            # check if the game is over
            if self.winsFor(nextCheckerToMove):
                print(self)
                print('\n' + nextCheckerToMove + ' wins! Congratulations!\n\n')
                break
            if self.isFull():
                print(self)
                print('\nThe game is a draw.\n\n')
                break

            # swap players
            if nextCheckerToMove == 'X':
                nextCheckerToMove = 'O'
            else:
                nextCheckerToMove = 'X'

        print('Come back soon 4 more!')



    def playGame(self, pForX, pForO, ss = False):
        """Plays a game of Connect Four.
            p1 and p2 are objects of type Player OR
            the string 'human'.
            If ss is True, it will "show scores" each time.
        """

        nextCheckerToMove = 'X'
        nextPlayerToMove = pForX

        while True:

            # print the current board
            print(self)

            # choose the next move
            if nextPlayerToMove == 'human':
                col = -1
                while not self.allowsMove(col):
                    col = int(input('Next col for ' + nextCheckerToMove + ': '))
            else: # it's a computer player
                if ss:
                    scores = nextPlayerToMove.scoresFor(self)
                    print((nextCheckerToMove + "'s"), 'Scores: ', [int(sc) for sc in scores])
                    print()
                    col = nextPlayerToMove.tiebreakMove(scores)
                else:
                    col = nextPlayerToMove.nextMove(self)

            # add the checker to the board
            self.addMove(col, nextCheckerToMove)

            # check if game is over
            if self.winsFor(nextCheckerToMove):
                print(self)
                print('\n' + nextCheckerToMove + ' wins! Congratulations!\n\n')
                break
            if self.isFull():
                print(self)
                print('\nThe game is a draw.\n\n')
                break

            # swap players
            if nextCheckerToMove == 'X':
                nextCheckerToMove = 'O'
                nextPlayerToMove = pForO
            else:
                nextCheckerToMove = 'X'
                nextPlayerToMove = pForX

        print('Come back 4 more!')


class Player:
    """An AI player for Connect Four."""

    def __init__(self, ox, tbt, ply):
        """Construct a player for a given checker, tie-breaking type,
           and ply."""
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__(self):
        """Create a string represenation of the player."""
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s
        
    def oppCh(self):
        """
        Returns the other kind of checker or playing piece, i.e., the piece being played by self's opponent
        """
        if self.ox == 'X':
            return 'O'
        return 'X'

    def scoreBoard(self, b):
        """
        Returns a single float value representing the score of the input b
        Returns 100.0 if the board b is a win for self. It should return 50.0 
        if it is neither a win nor a loss for self, and it should return 0.0 
        if it is a loss for self (i.e., the opponent has won).
        """
        if b.winsFor(self.ox):
            return 100.0
        elif b.winsFor(self.oppCh()):
            return 0.0
        else:
            return 50.0
    
    def tiebreakMove(self, scores):
        """ 
        Arguments: scores, a nonempty list of floating-point numbers
        Returns: its Column number, not the actual score. If there is 
        more than one highest score because of a tie, this method should 
        return the COLUMN number of the highest score appropriate to the 
        player's tiebreaking type. 
        """
        maxScore = max(scores)
        maxIndices = []
        for c in range(len(scores)):
            if scores[c] == maxScore:
                maxIndices += [c]
        if self.tbt == 'LEFT':
            return maxIndices[0]
        elif self.tbt == 'RIGHT':
            return maxIndices[len(maxIndices) - 1]
        else:
            return random.choice(maxIndices)
    """
    def scoresFor(self, b):
        """
        """
        Return a list of scores, with the cth score representing the 
        "goodness" of the input board after the player moves to column c. 
        And, "goodness" is measured by what happens in the game after 
        self.ply moves
        """
        """
        scores = [50] * b.width
        for c in range(b.width):
            while(self.ply >= 0):
                if b.allowsMove(c):
                    scores[c] = -1.0
                elif b.winsFor(self.ox):
                    scores[c] = 100.0
                elif b.winsFor(self.oppCh()):
                    scores[c] = 0.0
                elif self.ply == 0:
                    scores[c] = 50.0
                else:
                    b.addMove(c, self.ox)
                    if b.winsFor(self.ox):
                        scores[c] = 100.0
                    if b.winsFor(self.oppCh()):
                        scores[c] = 0.0
                op = Player(self.oppCh(), self.tbt, self.ply-1)

                self.ply += -1
        """
