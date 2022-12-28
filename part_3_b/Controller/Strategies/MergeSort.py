from Controller.Strategies.AbstractStrategy import AbstractStrategy
from View.GameStateENUM import GridObjects as go
import pygame
from math import floor
from copy import deepcopy

class MergeSort(AbstractStrategy):

  def __init__(self, *args):
    super().__init__(*args)
    
  def Sort(self, currentGrid, gridSize, currentPastGrids, currentPastGridsIndex):
    wallHeights = super().Sort(currentGrid)
    wallHeightsWithIndex = []

    #get original index
    for originalIndex in range(len(wallHeights)):
      wallHeightsWithIndex.append([wallHeights[originalIndex], originalIndex])

    #do the sort
    sortedWalls = self.MergeSort(wallHeightsWithIndex, currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)
    print(sortedWalls)

  def MergeSort(self, wallHeights, currentGrid, gridSize, currentPastGrids, currentPastGridsIndex):
    firstHalf = []
    secondHalf = []


    if len(wallHeights) == 1:
      return wallHeights

    #half up the arrays
    #from start to half
    for index in range(floor(len(wallHeights)/2)):
      firstHalf.append(wallHeights[index])
    #from half to end
    for index in range(floor(len(wallHeights)/2), len(wallHeights)):
      secondHalf.append(wallHeights[index])
    
    print("1st:", firstHalf)
    print("2nd:", secondHalf)





    #recursion
    firstHalf = self.MergeSort(firstHalf, currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)
    print("firstHalf recursion done")
    secondHalf = self.MergeSort(secondHalf, currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)
    print("secondHalf recursion done")

    return self.Merge(firstHalf, secondHalf, firstHalf[0][1], currentGrid, currentPastGrids, currentPastGridsIndex)

  def Merge(self, firstHalf, secondHalf, startingIndex, currentGrid, currentPastGrids, currentPastGridsIndex):
    sortedArray = []

    #compare the first index of the two arrays. whatever is smaller gets appended to the sorted array
    while firstHalf and secondHalf:
      if firstHalf[0][0] > secondHalf[0][0]:
        sortedArray.append(secondHalf[0])  
        secondHalf.pop(0)
      else:
        sortedArray.append(firstHalf[0])  
        firstHalf.pop(0)
      
      

    #send the rest of the indexes to the sorted array
    while firstHalf:
      sortedArray.append(firstHalf[0]) 
      firstHalf.pop(0)

    while secondHalf:
      sortedArray.append(secondHalf[0])  
      secondHalf.pop(0)

    self.SwapIndexes(currentGrid, startingIndex, sortedArray, currentPastGrids, currentPastGridsIndex)
    print("sorted:", sortedArray)
    return sortedArray

  def SwapIndexes(self, currentGrid, startingIndex, sortedArray, currentPastGrids, currentPastGridsIndex):
    print(startingIndex)
    #swap grid indecies
    clock = pygame.time.Clock()
    nextIndex = 0
    for i in range(len(sortedArray)):
      for gridRow in range(len(currentGrid)):
        currentGrid[gridRow].insert(startingIndex, currentGrid[gridRow][sortedArray[0][1]])
        if startingIndex < sortedArray[0][1]:
          currentGrid[gridRow].pop(sortedArray[0][1] + 1)
        else:
          currentGrid[gridRow].pop(sortedArray[0][1])
        for event in pygame.event.get():      
          if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        pygame.display.update()
        clock.tick(10)
      print("startingIndex:", startingIndex)
      startingIndex += 1


      self.viewManager.modelManager.gridMetaData.ChangeGridData(currentGrid, False, False, False)
      self.viewManager.uiGrid.Draw(currentGrid, currentPastGrids, 0, 0, go.NOTHING, currentPastGridsIndex)