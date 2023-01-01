import pygame
from View.GameStateENUM import GameState as gs


class AbstractUISquare():

  def __init__(self, uiGrid):
    self.uiGrid = uiGrid
    self.gridSpace = None
    self.leftClicked = False
    self.rightClicked = False

  def Draw(self, gameWindow, color, lineStartPositionx, lineStartPositiony, distanceBetweenRows):
    #location and size of square
    positions = [lineStartPositionx, lineStartPositiony, distanceBetweenRows, distanceBetweenRows]

    #draw square
    self.gridSpace = pygame.draw.rect(gameWindow, color, positions)
    return distanceBetweenRows, self.gridSpace

  def ClickGrid(self, mouseX, mouseY, gridRow, square, squareSpace, currentGridIndex, currentGridObject, currentGrid, pastGrids):
    if squareSpace != 0 and squareSpace.collidepoint(mouseX, mouseY) == True:
      if pygame.mouse.get_pressed()[0] == 1:
        #print("square clicked:", gridRow, square)
        self.uiGrid.viewManager.controllerManager.gridObjectController.Place(currentGridIndex, currentGridObject, currentGrid, pastGrids, self.leftClicked)
        self.leftClicked = True
      if pygame.mouse.get_pressed()[2] == 1:
        #print("square erased:", gridRow, square)
        self.uiGrid.viewManager.controllerManager.gridObjectController.Erase(currentGridIndex, currentGridObject, currentGrid, pastGrids, self.rightClicked)
        self.rightClicked = True
    else:
      return

  def UnclickGrid(self, pastGrids, currentGrid, currentPastGridsIndex):
    if pygame.mouse.get_pressed()[0] == 0 and self.leftClicked == True and self.rightClicked == False:
      self.leftClicked = False
      if currentPastGridsIndex != None:
        self.uiGrid.viewManager.controllerManager.gridObjectController.UnclickToSavePastGrids(pastGrids, currentGrid, currentPastGridsIndex)
        self.uiGrid.viewManager.ChangeGameState(gs.CREATING_MAZE)
    if pygame.mouse.get_pressed()[2] == 0 and self.rightClicked == True and self.leftClicked == False:
      self.rightClicked = False
      if currentPastGridsIndex != None:
        self.uiGrid.viewManager.controllerManager.gridObjectController.UnclickToSavePastGrids(pastGrids, currentGrid, currentPastGridsIndex)
        self.uiGrid.viewManager.ChangeGameState(gs.CREATING_MAZE)
    
