import pygame
from View.UISquare.AbstractUISquare import AbstractUISquare
from View.GameStateENUM import GridObjects as go
from View.UISquare.SquareData import square

class UIPath(AbstractUISquare):

  def __init__(self, uiGrid, *args):
    super().__init__(uiGrid, *args)
    self.color = square["path"]["color"]

  def Draw(self, gameWindow, currentGrid, gridRow, square, lineStartPositionx, lineStartPositiony, distanceBetweenRows):
    if currentGrid[gridRow][square] == go.PATH:
      returnValue = super().Draw(gameWindow, self.color, lineStartPositionx, lineStartPositiony, distanceBetweenRows)
      return returnValue
    else:
      return 0, 0

  def ClickGrid(self, mouseX, mouseY, gridRow, square, squareSpace, currentGridIndex, currentGridObject, currentGrid, pastGrids):
    #print("path")
    return super().ClickGrid(mouseX, mouseY, gridRow, square, squareSpace, currentGridIndex, currentGridObject, currentGrid, pastGrids)

  def UnclickGrid(self, pastGrids, currentGrid, currentPastGridsIndex):
    return super().UnclickGrid(pastGrids, currentGrid, currentPastGridsIndex)