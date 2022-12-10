import pygame
from View.UIButtons.AbstractUIButton import AbstractUIButton
from GameStateENUM import GameState as gs

class UILoadButton(AbstractUIButton):

  def __init__(self, *args):
    super().__init__(*args)
    

  def Draw(self, viewManager, background, buttonColor, buttonText, buttonWidth, buttonHeight, displayX, displayY):
    super().Draw()
    return gs.CREATING_MAZE

  def ClickButton(self):
    print("wip")