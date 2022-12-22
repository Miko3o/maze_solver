import pygame
from View.GameStateENUM import GridObjects as go

from View.UISquare.UIFinder import UIFinder
from View.UISquare.UIGoal import UIGoal
from View.UISquare.UINothing import UINothing
from View.UISquare.UIPath import UIPath
from View.UISquare.UISolver import UISolver
from View.UISquare.UIWall import UIWall

class UIGrid():

  def __init__(self, gameWindow, viewManager, currentGridObject):
    #window and manager
    self.gameWindow = gameWindow
    self.viewManager = viewManager

    #UISquares
    self.uiFinder = UIFinder(self)
    self.uiGoal = UIGoal(self)
    self.uiNothing = UINothing(self)
    self.uiPath = UIPath(self)
    self.uiSolver = UISolver(self)
    self.uiWall = UIWall(self)

    #UISquares in Array
    self.uiSquareList = [self.uiFinder, self.uiGoal, self.uiNothing, self.uiPath, self.uiSolver, self.uiWall]
    
    #creating grid
    self.gridBackground = pygame.draw.rect(self.gameWindow, (240, 240, 240), [160, 60, 280, 280])

    #clicked
    self.clicked = False
    self.gridSquareClicked = False

    #grid info
    self.currentGridIndex = (0, 0)
    self.currentGridObject = currentGridObject


  

  def Draw(self, currentGrid, pastGrids, mouseX, mouseY, currentGridObject, currentPastGridsIndex):
    #grid background
    self.gridBackground = pygame.draw.rect(self.gameWindow, (240, 240, 240), [160, 60, 280, 280])
    self.currentGridObject = currentGridObject
    distanceBetweenRows = 280 / len(currentGrid)
    

    #squares
    self.DrawSquaresHandler(160, 60, distanceBetweenRows, currentGrid, pastGrids, mouseX, mouseY, currentGridObject, currentPastGridsIndex)

    #lines
    self.DrawLinesHandler(160, 60, distanceBetweenRows, currentGrid, currentGridObject)
    


  
  def ClickGrid(self, mouseX, mouseY):
    #button on click
    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and self.gridSquareClicked == True:
      self.clicked = True
      print("grid clicked")
      return True
    else:
      return False
        
    
  def UnclickGrid(self, mouseX, mouseY):
    #button off click
    if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
      print("grid unclicked")
      self.clicked = False
      self.gridSquareClicked = False
      return False
    else:
      return False



  
  def DrawLinesHandler(self, lineStartPositionx, lineStartPositiony, distanceBetweenRows, currentGrid, currentGridObject):
    #grid lines
    for x in range(len(currentGrid[0])):
      lineStartPositionx += distanceBetweenRows
      pygame.draw.line(self.gameWindow, (0, 0, 0), (lineStartPositionx, 60), (lineStartPositionx, 340))
                  
    for y in range(len(currentGrid)):
      lineStartPositiony += distanceBetweenRows
      pygame.draw.line(self.gameWindow, (0, 0, 0), (160, lineStartPositiony), (440, lineStartPositiony))

    #grid outline
    pygame.draw.lines(self.gameWindow, (0, 0, 0), True, [(160, 60), (160, 340), (440, 340), (440, 60)], 2)



  
  def DrawSquaresHandler(self, lineStartPositionx, lineStartPositiony, distanceBetweenRows, currentGrid, pastGrids, mouseX, mouseY, currentGridObject, currentPastGridsIndex):  
    for gridRow in range(len(currentGrid)):
      for square in range(len(currentGrid[gridRow])):
        #drawing squares
        for squareMethod in self.uiSquareList:
          

          #draw square
          lineStartPositionxANDIndexSquareTuple = squareMethod.Draw(self.gameWindow, currentGrid, gridRow, square, lineStartPositionx, lineStartPositiony, distanceBetweenRows)
          lineStartPositionxANDIndexSquare = list(lineStartPositionxANDIndexSquareTuple)
          #print(lineStartPositionxANDIndexSquare[0])
          lineStartPositionx += lineStartPositionxANDIndexSquare[0]
          #lineStartPositionx = 160 + (square*distanceBetweenRows)
          
          #click square
          self.currentGridIndex = (gridRow, square)
          squareMethod.ClickGrid(mouseX, mouseY, gridRow, square, lineStartPositionxANDIndexSquare[1], self.currentGridIndex, self.currentGridObject, currentGrid, pastGrids)
          if squareMethod != self.uiNothing:
            squareMethod.UnclickGrid(pastGrids, currentGrid, currentPastGridsIndex)
          

            

        

      lineStartPositionx = 160
      lineStartPositiony += distanceBetweenRows
    return self.currentGridIndex, False, None #False = not clicked