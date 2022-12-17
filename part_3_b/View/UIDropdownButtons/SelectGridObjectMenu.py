import pygame
from View.UIDropdownButtons.AbstractUIDropdownMenu import AbstractUIDropdownMenu
from View.GameStateENUM import GameState as gs, ButtonType as bt

class SelectGridObjectMenu(AbstractUIDropdownMenu):

  def __init__(self, *args):
    super().__init__(*args)
    

  def Draw(self, mouseX, mouseY):
    super().Draw(mouseX, mouseY)


  def ClickButton(self, mouseX, mouseY):
    super().ClickButton(mouseX, mouseY)


  def UnclickOption(self, mouseX, mouseY):
    objectChoice = super().UnclickOption(mouseX, mouseY)
    if objectChoice != 0:
      self.viewManager.ChangeGridObject(objectChoice)

