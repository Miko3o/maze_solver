from Controller.Strategies.AbstractStrategy import AbstractStrategy
from View.GameStateENUM import GridObjects as go
import pygame
from random import randint

class QuickSort(AbstractStrategy):

  def __init__(self, *args):
    super().__init__(*args)
    
  def Sort(self, currentGrid, gridSize, currentPastGrids, currentPastGridsIndex):
    wallHeights = super().Sort(currentGrid)
    print("starting array:", wallHeights)
    self.QuickSort(currentGrid, wallHeights, 0, len(wallHeights) - 1, gridSize, currentPastGrids, currentPastGridsIndex)
    print("final array:", wallHeights)

  def QuickSort(self, currentGrid, wallHeights, low, high, gridSize, currentPastGrids, currentPastGridsIndex):
    #if the lowest index is less than the highest index
    if low < high:
      #set the pivot location to the return value of partition
      pivotLocation = self.Partition(currentGrid, wallHeights, low, high, gridSize, currentPastGrids, currentPastGridsIndex)
      print("pivotLocation:", pivotLocation)
      print(wallHeights)
      #run the sort again but with the pivot location as the highest index
      self.QuickSort(currentGrid, wallHeights, low, pivotLocation - 1, gridSize, currentPastGrids, currentPastGridsIndex)
      #run the sort again but with the pivot location + 1 as the lowest index
      self.QuickSort(currentGrid, wallHeights, pivotLocation + 1, high, gridSize, currentPastGrids, currentPastGridsIndex)

  def Partition(self, currentGrid, wallHeights, low, high, gridSize, currentPastGrids, currentPastGridsIndex):
    clock = pygame.time.Clock()
    #set the index of the pivot to be switched with the highest index
    pivotToSwitch = self.GetRandInt(low, high)
    print("pivot to switch:", pivotToSwitch)
    print("high:", high)
    #swap the pivot with the highest index
    self.SwapIndexes(currentGrid, wallHeights, pivotToSwitch, high, currentPastGrids, currentPastGridsIndex)
    print("pivot to end:", wallHeights)

    #set pivot as whatever is in the highest index index
    pivot = wallHeights[high]
    print("pivot:", "index", high, "number", pivot)
    #set leftwall as the lowest index number and rightWall as the second to last index
    leftWall = low
    rightWall = high - 1

    #while the leftWall and rightWall haven't passed each other yet
    while leftWall <= rightWall:
      print("leftWall:", wallHeights[leftWall])
      print("rightWall:", wallHeights[rightWall])
      print("pivot:", pivot)
      #if the leftWall is smaller than the pivot, move right one and if the rightWall is bigger than the pivot, move left one
      if wallHeights[leftWall] <= pivot:
        leftWall += 1
      elif wallHeights[rightWall] >= pivot:
        rightWall -= 1
      #if leftWall can't go right anymore and if rightWall can't move left anymore, swap the leftWall and rightWall
      else:
        self.SwapIndexes(currentGrid, wallHeights, rightWall, leftWall, currentPastGrids, currentPastGridsIndex)
        print("swapped highs and lows:", wallHeights)

    #swap the pivot and the leftWall
    self.SwapIndexes(currentGrid, wallHeights, high, leftWall, currentPastGrids, currentPastGridsIndex)
    print("leftWall and pivot have been swapped")

    #pygame UI tick speed
    for event in pygame.event.get():      
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    pygame.display.update()
    clock.tick(5)

    #return leftwall
    return leftWall

  def GetRandInt(low, high):
    return randint(low, high)



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