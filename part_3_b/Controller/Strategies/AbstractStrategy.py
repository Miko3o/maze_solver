from View.GameStateENUM import GridObjects as go
from copy import deepcopy


class AbstractStrategy():

  def __init__(self, viewManager, gameWindow):
    self.viewManager = viewManager
    self.gameWindow = gameWindow

  def Solve(self):
    print("wip")

  def Sort(self, currentGrid):
    #set mazewalls to a list of arrays
    wallHeights = []
    currentSquare = 0
    while currentSquare < len(currentGrid):
      numberOfWallBlocks = 0
      for gridRow in range(len(currentGrid)):
        for square in range(len(currentGrid[gridRow])):
          if currentGrid[gridRow][square] == go.WALL and square == currentSquare:
            numberOfWallBlocks += 1
      wallHeights.append(numberOfWallBlocks)
      currentSquare += 1
    print(wallHeights)
    return wallHeights
      
