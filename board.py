# Writing game described at 
# https://inventwithpython.com/invent4thed/chapter13.html
# Using object oriented and functional principals instead of
# just functions

FOUR_SPACES = '    '
THREE_SPACES = '   '

class Board:
  def __init__(self, height=15, width=60):
    self.height = height
    self.width = width
    self.widthTens = round(width/10)

  def getNewBoard(self):
  # Create a width x height board.
    board = []
    for x in range(self.width):
      board.append([])
      for y in range(self.height):
        board[x].append("~")
    return board
  
  def drawBoard(self, board):
    self.drawXTens()
    self.drawXOnes()
    print()
    self.drawBoardMiddle(board)
    print()
    self.drawXOnes()
    self.drawXTens()

  def drawXTens(self):
    xTens = FOUR_SPACES
    for i in range(1, self.widthTens):
      xTens += (' ' * 9) + str(i)
    print(xTens)

  def drawXOnes(self):
    xOnes = THREE_SPACES + ('0123456789' * self.widthTens)
    print(xOnes)

  def drawBoardMiddle(self, board):
    for row in range(self.height):
      extraSpace = ''
      if row < 10:
          extraSpace = ' '
      boardRow = ''
      for column in range(self.width):
        boardRow += board[column][row]
      print('%s%s %s %s' % (extraSpace, row, boardRow, row))

board = Board()
theBoard = board.getNewBoard()
board.drawBoard(theBoard)

