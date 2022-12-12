import pygame
from View.UIDropdownButtons.AbstractUIDropdownButton import AbstractUIDropdownButton
from View.GameStateENUM import GameState as gs, ButtonType as bt

class SelectGridObjectDropdown(AbstractUIDropdownButton):

  def __init__(self, *args):
    super().__init__(*args)
    

  def Draw(self, mouseX, mouseY):
    super().Draw(mouseX, mouseY)


  def ClickButton(self, mouseX, mouseY):
    super().ClickButton(mouseX, mouseY)


  def UnclickButton(self, currentGrid, gridSize, currentPastGrids, currentPastGridsIndex):
    return super().UnclickButton(currentGrid, gridSize, bt.SELECT_OBJECT)
