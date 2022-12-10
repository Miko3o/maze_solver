import pygame
from View.UIButtons.AbstractUIButton import AbstractUIButton
from View.GameStateENUM import GameState as gs

class UILoadButton(AbstractUIButton):

  def __init__(self, *args):
    super().__init__(*args)
    

  def Draw(self, mouseX, mouseY):
    super().Draw(mouseX, mouseY)
    return gs.CREATING_MAZE

  def ClickButton(self, mouseX, mouseY):
    super().ClickButton(mouseX, mouseY)
    return gs.CREATING_MAZE

  def UnclickButton(self, currentGrid, gridSize, currentPastGrids):
    self.viewManager.controllerManager.loadMazeController.LoadMaze()
    return super().UnclickButton()
