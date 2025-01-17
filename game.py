# Writing game described at 
# https://inventwithpython.com/invent4thed/chapter13.html
# Using object oriented and functional principals instead of
# just functions

class Board:
  def __init__(self, height=15, width=60):
    self.height = height
    self.width = width

  def getNewBoard(self):
  # Create a width x height board.
    board = []
    for x in range(self.width):
      board.append([])
      for y in range(self.height):
        board[x].append("~")
    return board
    
board = Board()
theBoard = board.getNewBoard()
print(theBoard)
