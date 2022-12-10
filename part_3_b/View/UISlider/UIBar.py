import pygame
from View.GameStateENUM import GameState as gs

class UIBar():

  def __init__(self, background):

    #button properties
    self.background = background
  
  def Draw(self):
    pygame.draw.line(self.background, (0, 0, 0), (475, 300), (565, 300) , 4)