import pygame
from GameStateENUM import GameState as gs

class AbstractUIButton():

  def __init__(self, background, buttonColor, buttonText, buttonWidth, buttonHeight, displayX, displayY):
    
    self.background = background
    self.buttonColor = buttonColor
    self.buttonText = buttonText
    self.buttonWidth = buttonWidth
    self.buttonHeight = buttonHeight
    self.displayX = displayX
    self.displayY = displayY
    

  def Draw(self):
    pygame.draw.rect(self.background, (self.buttonColor), [self.displayX, self.displayY, self.buttonWidth, self.buttonHeight])
    print(self.buttonText)

    
    return gs.CREATING_MAZE

  def ClickButton(self):
    print("wip")