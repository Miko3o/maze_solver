from View.GameStateENUM import GridObjects as go
import pygame


class GravityController():

  def __init__(self, viewManager):
    self.viewManager = viewManager

  def Gravity(self, currentGrid):
    #delete grid objects except walls
    for gridRow in range(len(currentGrid)):
      for square in range(len(currentGrid[gridRow])):
        if currentGrid[gridRow][square] != go.NOTHING and currentGrid[gridRow][square] != go.WALL:
          currentGrid[gridRow][square] = go.NOTHING
    self.viewManager.modelManager.gridMetaData.ChangeGridData(currentGrid, False, False, False)
    clock = pygame.time.Clock()
    while True:
      scanComplete = True
      for gridRow in range(len(currentGrid) - 1):
        for square in range(len(currentGrid[gridRow])):
          #get index of square under
          underSquare = [square, gridRow - 1]
          


          if currentGrid[gridRow + 1][square] == go.NOTHING and currentGrid[gridRow][square] == go.WALL and gridRow + 1 != -1:
            currentGrid[gridRow][square] = go.NOTHING
            currentGrid[gridRow + 1][square] = go.WALL
            self.viewManager.modelManager.gridMetaData.ChangeGridData(currentGrid, False, False, False)
            self.viewManager.uiGrid.Draw(currentGrid, [], 0, 0, go.NOTHING, None)
            scanComplete = False
      
        for event in pygame.event.get():      
          if event.type == pygame.QUIT:
              pygame.quit()
              exit()
        pygame.display.update()
        clock.tick(70)
      if scanComplete == True:
        break
          
