import random

def inarow_Neast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading east and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading south and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading northeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start - (N-1) < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading southeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True


class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # the string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # bottom of the board

        # and the numbers underneath here

        s += '\n'
        for col in range (self.width):
            s += ' ' + str(col%10)

        return s       # the board is complete, return it
    
    def addMove(self, col, ox):
        """
        This method takes two arguments: the first, col, represents 
        the index of the column to which the checker will be added. 
        The second argument, ox, will be a 1-character string representing 
        the checker to add to the board. That is, ox should either be 'X' or 'O'
        """

        H = self.height
        for row in range(H):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return
                
        self.data[H-1][col] = ox

    def clear(self):
        """ clears the board """

        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = ' '

    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    
    def allowsMove(self,c):
        """
            return True if the calling object (of type Board) does allow 
            a move into column c. It returns False if column c is not a legal 
            column number for the calling object. It also returns False if 
            column c is full. Thus, this method should check to be sure that 
            c is within the range from 0 to the last column and make sure that
             there is still room left in the column
        """

        if c > self.width or c < 0:
            return False
        if self.data[0][c] != ' ':
            return False
        
        return True
    
    def isFull(self):
        """
            return True if the calling object (of type Board) 
            is completely full of checkers. It should return False otherwise
        """

        for row in range(self.height):
            for col in range(self.width):
                if self.data[row][col] == ' ':
                    return False
        
        return True
    
    def delMove(self, col):
        """
            should do the opposite of addMove. It should remove the top checker 
            from the column c. If the column is empty, then delMove should do 
            nothing
        """

        H = self.height
        for row in range(H):
            if self.data[row][col] == 'X' or self.data[row][col] == 'O':
                self.data[row][col] = ' '
                return


            

    def winsFor(self, ox):
        """
            This method's argument ox is a 1-character checker: either 
            'X' or 'O'. It should return True if there are four checkers 
            of type ox in a row on the board. It should return False othwerwise
        """

        H = self.height
        W = self.width
        D = self.data

        for row in range(0, H):
            for col in range(0, W):
                if inarow_Neast(ox, row, col, self.data, 4):
                    return True
                if inarow_Nsouth(ox, row, col, self.data, 4):
                    return True
                if inarow_Nnortheast(ox, row, col, self.data, 4):
                    return True
                if inarow_Nsoutheast(ox, row, col, self.data, 4):
                    return True
        
        return False

    def hostGame(self):
        """
            It should host a game of Connect Four, using the methods 
            listed above to do so. In particular, it should alternate turns
             between 'X' (who will always go first) and 'O' (who will always 
             go second). It should ask the user (with the input function) to
            select a column number for each move.
        """
        print("Welcome to Connect Four!")
        print(self)

        while(True):
            users_col = int(input("Player X, choose a column: "))
            while not self.allowsMove(users_col):
                users_col = int(input("Player X, choose a column: "))

            self.addMove(users_col, 'X')
            if self.winsFor('X') == True:
                print(self)
                print("Player X has won!")
                break
            if self.isFull() == True:
                print(self)
                print("Board is full...")
                break

            print(self)



            comp_col = self.aiMove('O')
            

            self.addMove(comp_col, 'O')
            if self.winsFor('O') == True:
                print(self)
                print("Player O has won!") 
                break
            if self.isFull() == True:
                print(self)
                print("Board is full...")
                break
            print(self)
    
    def colsToWin(self, ox):
        """
        take one argument, ox, which will be either the string 'X' or the string 'O'
         return the list of columns where ox can move in the next turn in order to win 
         and finish the game. The columns should be in numeric order
        """

        list = []

        for col in range(self.width):
            if(self.allowsMove(col)):
                self.addMove(col, ox)
                if(self.winsFor(ox)):
                    list += [col]
                self.delMove(col)
        
        return list

    def aiMove(self, ox):

        """
        accept a single argument, ox, which will be either the string 'X' or the string 'O'
        return a single integer, which must be a legal column in which to make a move. AND
        If there is a way for ox to win, then aiMove MUST return that move (that column number). It
        must win when it can. There may be more than one way to win: in this case, any one of those 
        winning column moves may be returned.
        If there is NO way for ox to win, but there IS a way for ox to block the opponent's 
        four-in-a-row, then aiMove MUST return a move that blocks its opponent's four-in-a-row. 
        Again, it should not look more than one move ahead for its opponent. If there are no wins,
        but multiple ways to block the opponent, then aiMove should return any one of those ways to
        block the opponent. (Even though the opponent might win in a different way.)
        If there is NO way for ox to win NOR a way for ox to block the opponent from winning, 
        then aiMove should return a move of your (the programmer's) choice—but it must be a legal move. 
        We won't call aiMove when the board is full.
        """

        d = {}
        d['X'] = self.colsToWin('X')
        d['O'] = self.colsToWin('O')

        if(len(d[ox]) > 0 ):
            return random.choice(d[ox])
        elif (len(d[ox]) == 0):
            if ox == 'X':
                if len(d['O'] > 0):
                    return random.choice(d['O'])
            else:
                 if len(d['X']) > 0:
                    return random.choice(d['X'])

        move = random.choice(range(self.width))
        while not self.allowsMove(move):
            move = random.choice(range(self.width))
        return move

    