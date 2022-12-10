import pygame
from View.UIDropdownButtons.AbstractUIDropdownMenu import AbstractUIDropdownMenu
from View.GameStateENUM import GameState as gs

class SolveAlgorithmMenu(AbstractUIDropdownMenu):

  def __init__(self, *args):
    super().__init__(*args)
    

  def Draw(self, mouseX, mouseY):
    super().Draw(mouseX, mouseY)


  def ClickButton(self, mouseX, mouseY):
    super().ClickButton(mouseX, mouseY)


  def UnclickButton(self, mouseX, mouseY):
    return super().UnclickButton(mouseX, mouseY)
