import pygame
from View.UIDropdownButtons.AbstractUIDropdownButton import AbstractUIDropdownButton
from View.GameStateENUM import GameState as gs, ButtonType as bt

class SortAlgorithmDropdown(AbstractUIDropdownButton):

  def __init__(self, *args):
    super().__init__(*args)
    

  def Draw(self, mouseX, mouseY):
    super().Draw(mouseX, mouseY)


  def ClickButton(self, mouseX, mouseY):
    super().ClickButton(mouseX, mouseY)


  def UnclickButton(self, currentGrid, gridSize, currentPastGrids, currentPastGridsIndex, gameState):
    if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True and gameState == gs.SORTING_SOLVED_MAZE:
      self.viewManager.ChangeGameState(gs.PICKING_SORTING_ALG)
      self.clicked = False
    else:
      self.viewManager.ChangeGameState(gs.SORTING_SOLVED_MAZE)