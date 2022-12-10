from GameManager.GameStateENUM import GameState as gs, LoopState as ls
from View.ViewManager import ViewManager

import pygame
from sys import exit

pygame.init()

class GameManager():

  def __init__(self):

    #creating window
    self.gameWindow = pygame.display.set_mode((600, 400))
    
    #managers
    self.viewManager = ViewManager(self.gameWindow)
    #clock
    self.clock = pygame.time.Clock()

    #setting states
    self.gameState = gs.CREATING_MAZE
    self.loopState = ls.IN_APP




  def Init(self):
    
    #setting up window
    self.gameWindow.fill('White')

    #states
    while self.loopState == ls.IN_APP:
      if self.gameState == gs.CREATING_MAZE:
        self.viewManager.UIGrid.Draw(self.gameWindow)
        self.viewManager.UILoadButton.Draw(self.gameWindow, "Blue", "hi", 50, 20, 10, 30)
        print("wip")

      if self.gameState == gs.PICKING_SOLVING_ALG:
        print("wip")

      if self.gameState == gs.SORTING_SOLVED_MAZE:
        print("wip")

      if self.gameState == gs.PICKING_SORTING_ALG:
        print("wip")

      if self.gameState == gs.CLOSING_APP:
        print("wip")

        
      #quitting pygame
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
      
      #updates the display surface
      pygame.display.update()
      self.clock.tick(60)