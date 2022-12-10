import pygame
#from GameStateENUM import GameState as gs

class UIGrid():

  def __init__(self):

    
    #creating grid
    self.gridBackground = pygame.Surface((280,280))

  def Draw(self, background):
    #grid background
    self.gridBackground.fill((240, 240, 240))
    background.blit(self.gridBackground, (160, 60))

    #grid lines and other stuff
    print("wip")

    
    return "hi"
