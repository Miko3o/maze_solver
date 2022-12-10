import pygame
from View.UISquare.AbstractUISquare import AbstractUISquare
from View.GameStateENUM import GridObjects as go
from View.UISquare.SquareData import square

class UINothing(AbstractUISquare):

  def __init__(self, uiGrid, *args):
    super().__init__(uiGrid, *args)
    self.color = square["nothing"]["color"]

  def Draw(self, gameWindow, currentGrid, gridRow, square, lineStartPositionx, lineStartPositiony, distanceBetweenRows):
    if currentGrid[gridRow][square] == go.NOTHING:
      returnValue = super().Draw(gameWindow, self.color, lineStartPositionx, lineStartPositiony, distanceBetweenRows)
      return returnValue
    else:
      return 0, 0

  def ClickGrid(self, mouseX, mouseY, gridRow, square, squareSpace, currentGridIndex, currentGridObject, currentGrid, pastGrids):
    #print("nothing")
    return super().ClickGrid(mouseX, mouseY, gridRow, square, squareSpace, currentGridIndex, currentGridObject, currentGrid, pastGrids)

  def UnclickGrid(self, pastGrids, currentGrid):
    return super().UnclickGrid(pastGrids, currentGrid)