from Controller.Strategies.AbstractStrategy import AbstractStrategy
from View.GameStateENUM import GridObjects as go
import pygame

class SelectionSort(AbstractStrategy):

  def __init__(self, *args):
    super().__init__(*args)
    
  def Sort(self, currentGrid, gridSize, currentPastGrids, currentPastGridsIndex):
    wallHeights = super().Sort(currentGrid)
    clock = pygame.time.Clock()

    #STEP 1: iterate through whole array
    for i in range(len(wallHeights)):
      
      #STEP 2: find minimum
      minHeight = i
      for nextIndex in range(i + 1, len(wallHeights)):
        if wallHeights[minHeight] > wallHeights[nextIndex]:
          minHeight = nextIndex

      #STEP 3: swap the minimum with the first index
      self.SwapIndexes(currentGrid, wallHeights, i, minHeight, currentPastGrids, currentPastGridsIndex)

      #clock
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
      pygame.display.update()
      clock.tick(10)

    print(wallHeights)


  def SwapIndexes(self, currentGrid, wallHeights, currentIndex, minHeight, currentPastGrids, currentPastGridsIndex):
    #swap list indecies
    indexToBeSwapped = wallHeights[currentIndex]
    wallHeights[currentIndex] = wallHeights[minHeight]
    wallHeights[minHeight] = indexToBeSwapped
    
    #swap grid indecies
    for gridRow in range(len(currentGrid)):
        gridIndexToBeSwapped = currentGrid[gridRow][currentIndex]
        currentGrid[gridRow][currentIndex] = currentGrid[gridRow][minHeight]
        currentGrid[gridRow][minHeight] = gridIndexToBeSwapped

    self.viewManager.modelManager.gridMetaData.ChangeGridData(currentGrid, False, False, False)
    self.viewManager.uiGrid.Draw(currentGrid, currentPastGrids, 0, 0, go.NOTHING, currentPastGridsIndex)