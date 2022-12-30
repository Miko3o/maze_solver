from Controller.Strategies.AbstractStrategy import AbstractStrategy
from View.GameStateENUM import GridObjects as go
import pygame
from math import floor
from copy import deepcopy

class MergeSort(AbstractStrategy):

  def __init__(self, *args):
    super().__init__(*args)
    self.realSortedWalls = []
    self.currentSortingIndex = 0
    self.level = 0
    self.levelSaver = 0
    self.levelChangeStart = 0
    
  def Sort(self, currentGrid, gridSize, currentPastGrids, currentPastGridsIndex):
    wallHeights = super().Sort(currentGrid)
    self.realSortedWalls = wallHeights
    #wallHeightsWithIndex = []

    #get original index
    #for originalIndex in range(len(wallHeights)):
      #wallHeightsWithIndex.append([wallHeights[originalIndex], originalIndex])

    #do the sort
    sortedWalls = self.MergeSort(wallHeights, currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)
    print(sortedWalls)

  def MergeSort(self, wallHeights, currentGrid, gridSize, currentPastGrids, currentPastGridsIndex):
    newWallHeights = [[], []]


    if len(wallHeights) == 1:
      self.level += 1
      return wallHeights

    #half up the arrays
    #from start to half
    for index in range(floor(len(wallHeights)/2)):
      newWallHeights[0].append(wallHeights[index])
    #from half to end
    for index in range(floor(len(wallHeights)/2), len(wallHeights)):
      newWallHeights[1].append(wallHeights[index])
    
    print(newWallHeights)
    print("1st:", newWallHeights[0])
    print("2nd:", newWallHeights[1])

    self.level += 1
    print("level:", self.level)
    

    #recursion
    newWallHeights[0] = self.MergeSort(newWallHeights[0], currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)
    print("firstHalf recursion done")
    self.level -= 1
    

    newWallHeights[1] = self.MergeSort(newWallHeights[1], currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)
    print("secondHalf recursion done")

    self.level -= 1

    

    

    return self.Merge(newWallHeights[0], newWallHeights[1], newWallHeights[0][0], currentGrid, currentPastGrids, currentPastGridsIndex)

  def Merge(self, firstHalf, secondHalf, startingIndex, currentGrid, currentPastGrids, currentPastGridsIndex):
    sortedArray = []


    #compare the first index of the two arrays. whatever is smaller gets appended to the sorted array
    while firstHalf and secondHalf:
      if firstHalf[0] > secondHalf[0]:
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

    if self.level == self.levelSaver:
      self.realSortedWalls[self.currentSortingIndex] = sortedArray
      self.realSortedWalls.pop(self.currentSortingIndex + 1)
      self.currentSortingIndex += 1
    elif self.level == self.levelSaver + 1:
      self.realSortedWalls[self.levelChangeStart] = sortedArray
      self.realSortedWalls.pop(self.currentSortingIndex + 1)
      self.currentSortingIndex += 1
      self.levelSaver = self.level
    else:
      self.realSortedWalls[0] = sortedArray
      self.currentSortingIndex = 0
      self.realSortedWalls.pop(self.currentSortingIndex + 1)
      self.currentSortingIndex += 1
      self.levelSaver = self.level
      self.levelChangeStart += 1


    print("WHOLE currentWalls:", self.realSortedWalls)
        
    


    #self.SwapIndexes(currentGrid, startingIndex, sortedArray, currentPastGrids, currentPastGridsIndex)
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