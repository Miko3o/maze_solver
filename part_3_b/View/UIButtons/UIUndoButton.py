import pygame
from View.UIButtons.AbstractUIButton import AbstractUIButton
from View.GameStateENUM import GameState as gs

class UIUndoButton(AbstractUIButton):

  def __init__(self, *args):
    super().__init__(*args)
    

  def Draw(self, mouseX, mouseY):
    super().Draw(mouseX, mouseY)
    return gs.CREATING_MAZE

  def ClickButton(self, mouseX, mouseY):
    super().ClickButton(mouseX, mouseY)
    return gs.CREATING_MAZE

  def UnclickButton(self, currentGrid, currentGridSize, currentPastGrids, currentPastGridsIndex):
    if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
      self.viewManager.controllerManager.undoController.Undo(currentGrid, currentGridSize, currentPastGrids, currentPastGridsIndex)
    return super().UnclickButton()