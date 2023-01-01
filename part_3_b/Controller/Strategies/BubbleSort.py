from Controller.Strategies.AbstractStrategy import AbstractStrategy
from View.GameStateENUM import GridObjects as go
import pygame
from copy import deepcopy

class BubbleSort(AbstractStrategy):

  def __init__(self, *args):
    super().__init__(*args)

  def Sort(self, currentGrid, gridSize, currentPastGrids, currentPastGridsIndex):
    wallHeights = super().Sort(currentGrid)
    clock = pygame.time.Clock()
    for i in range(len(wallHeights)):
      for currentIndex in range(len(wallHeights) - 1):
        if wallHeights[currentIndex] > wallHeights[currentIndex + 1]:
          self.SwapIndexes(currentGrid, wallHeights, currentIndex, gridSize, currentPastGrids, currentPastGridsIndex)
      for event in pygame.event.get():      
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
      pygame.display.update()
      clock.tick(10)
    print(wallHeights)

  def SwapIndexes(self, currentGrid, wallHeights, currentIndex, gridSize, currentPastGrids, currentPastGridsIndex):
      #swap list indecies
      indexToBeSwapped = wallHeights[currentIndex]
      wallHeights[currentIndex] = wallHeights[currentIndex + 1]
      wallHeights[currentIndex + 1] = indexToBeSwapped
      
      #swap grid indecies
      for gridRow in range(len(currentGrid)):
          gridIndexToBeSwapped = currentGrid[gridRow][currentIndex]
          currentGrid[gridRow][currentIndex] = currentGrid[gridRow][currentIndex + 1]
          currentGrid[gridRow][currentIndex + 1] = gridIndexToBeSwapped

      self.viewManager.modelManager.gridMetaData.ChangeGridData(currentGrid, False, False, False)
      self.viewManager.uiGrid.Draw(currentGrid, currentPastGrids, 0, 0, go.NOTHING, 1)

    
