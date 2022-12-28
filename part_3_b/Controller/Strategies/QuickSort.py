from Controller.Strategies.AbstractStrategy import AbstractStrategy
from View.GameStateENUM import GridObjects as go
import pygame

class QuickSort(AbstractStrategy):

  def __init__(self, *args):
    super().__init__(*args)
    
  def Sort(self, currentGrid, gridSize, currentPastGrids, currentPastGridsIndex):
    wallHeights = super().Sort(currentGrid)
    self.QuickSort(currentGrid, wallHeights, 0, len(wallHeights) - 1, gridSize, currentPastGrids, currentPastGridsIndex)

  def QuickSort(self, currentGrid, wallHeights, low, high, gridSize, currentPastGrids, currentPastGridsIndex):
    #if the lowest index is less than the highest index
    if low < high:
      #set the pivot location to the return value of partition
      pivotLocation = self.Partition(currentGrid, wallHeights, low, high, gridSize, currentPastGrids, currentPastGridsIndex)
      print("pivotLocation:", pivotLocation)
      #run the sort again but with the pivot location as the highest index
      self.QuickSort(currentGrid, wallHeights, low, pivotLocation, gridSize, currentPastGrids, currentPastGridsIndex)
      #run the sort again but with the pivot location + 1 as the lowest index
      self.QuickSort(currentGrid, wallHeights, pivotLocation + 1, high, gridSize, currentPastGrids, currentPastGridsIndex)

  def Partition(self, currentGrid, wallHeights, low, high, gridSize, currentPastGrids, currentPastGridsIndex):
    clock = pygame.time.Clock()
    #set pivot as whatever is in the lowest index
    pivot = wallHeights[low]
    print("pivot:", pivot)
    #set leftwall as the lowest index number
    leftwall = low
    #for i = low + 1 to high
    for i in range(low + 1, high):
      print("i:", i)
      #if the item in index i is less than the pivot, swap that item and whatever the leftwall is and add one to the leftwall
      if i < pivot:
        self.SwapIndexes(currentGrid, wallHeights, wallHeights[i], wallHeights[leftwall], currentPastGrids, currentPastGridsIndex)
    #swap the pivot and whatever is in leftwall
    self.SwapIndexes(currentGrid, wallHeights, pivot, wallHeights[leftwall], currentPastGrids, currentPastGridsIndex)

    #pygame tick
    for event in pygame.event.get():      
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    pygame.display.update()
    clock.tick(5)

    #return leftwall
    return leftwall



  def SwapIndexes(self, currentGrid, wallHeights, currentIndexItem, leftWall, currentPastGrids, currentPastGridsIndex):
    #swap list indecies
    indexToBeSwapped = wallHeights[currentIndexItem]
    wallHeights[currentIndexItem] = wallHeights[leftWall]
    wallHeights[leftWall] = indexToBeSwapped
    
    #swap grid indecies
    for gridRow in range(len(currentGrid)):
        gridIndexToBeSwapped = currentGrid[gridRow][currentIndexItem]
        currentGrid[gridRow][currentIndexItem] = currentGrid[gridRow][leftWall]
        currentGrid[gridRow][leftWall] = gridIndexToBeSwapped

    self.viewManager.modelManager.gridMetaData.ChangeGridData(currentGrid, False, False, False)
    self.viewManager.uiGrid.Draw(currentGrid, currentPastGrids, 0, 0, go.NOTHING, currentPastGridsIndex)