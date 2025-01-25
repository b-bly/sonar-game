# Writing game described at
# https://inventwithpython.com/invent4thed/chapter13.html
# Using object oriented and functional principals instead of
# just functions

import random
import math

FOUR_SPACES = '    '
THREE_SPACES = '   '


class Board:
    def __init__(self, y=15, x=60, numChests=3):
        self.y = y
        self.x = x
        self.xTens = round(x/10)
        self.numChests = numChests
        self.chests = []
        self.board = []

    def getNewBoard(self):
        # Create a x x y board.
        # TODO Save board in this class?
        board = []
        for x in range(self.x):
            board.append([])
            for y in range(self.y):
                board[x].append("~")
        self.board = board
        return board

    def drawBoard(self):
        board = self.board
        self.drawXTens()
        self.drawXOnes()
        print()
        self.drawBoardMiddle(board)
        print()
        self.drawXOnes()
        self.drawXTens()

    def drawXTens(self):
        xTens = FOUR_SPACES
        for i in range(1, self.xTens):
            xTens += (' ' * 9) + str(i)
        print(xTens)

    def drawXOnes(self):
        xOnes = THREE_SPACES + ('0123456789' * self.xTens)
        print(xOnes)

    def drawBoardMiddle(self):
        board = self.board
        for row in range(self.y):
            extraSpace = ''
            if row < 10:
                extraSpace = ' '
            boardRow = ''
            for column in range(self.x):
                boardRow += board[column][row]
            print('%s%s %s %s' % (extraSpace, row, boardRow, row))

    def getRandomChests(self):
        # Create a list of chest data structures (two-item lists of x, y int
        chests = []
        while len(chests) < self.numChests:
            newChest = [random.randint(0, self.x - 1),
                        random.randint(0, self.y)]
            if newChest not in chests:
                chests.append(newChest)
        self.chests = chests
        return chests

    def isOnBoard(self, x, y):
        return x >= 0 and x <= self.x and y >= 0 and y <= self.y

    def makeMove(self, x, y):
        board = self.board
        chests = self.chests
        smallestDistance = 100  # Any chest will be closer than 100.
        for cx, cy in chests:
            distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))
            if distance < smallestDistance:  # We want the closest treasure chest
                smallestDistance = distance
            smallestDistance = round(smallestDistance)
            if smallestDistance == 0:
                # xy is directly on a treasure chest!
                chests.remove([x, y])
                return 'You have found a sunken treasure chest!'
            else:
                if smallestDistance < 10:
                    board[x][y] = str(smallestDistance)
                    return 'Treasure detected at a distance of %s from the sonar device.' % (smallestDistance)
                else:
                    board[x][y] = 'X'
                    return 'Sonar did not detect anything. All treasure chests out of range.'

    def enterPlayerMove(self, previousMoves):
      # Let the player enter their move. Return a two-item list of int xy coordinates.
        print('Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)')
        while True:
            move = input()
            if move.lower() == 'quit':
                print('Thanks for playing!')
                sys.exit()
 
            move = move.split()
            if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and self.isOnBoard(int(move[0]), int(move[1])):
                if [int(move[0]), int(move[1])] in previousMoves:
                    print('You already moved there.')
                    continue
                return [int(move[0]), int(move[1])]
            print('Enter a number from 0 to 59, a space, then a number from 0 to 14.')

board = Board()
theBoard = board.getNewBoard()
board.drawBoard(theBoard)
print(board.getRandomChests())
