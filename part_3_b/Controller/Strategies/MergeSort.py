from Controller.Strategies.AbstractStrategy import AbstractStrategy
from View.GameStateENUM import GridObjects as go
import pygame
from math import ceil

class MergeSort(AbstractStrategy):

  def __init__(self, *args):
    super().__init__(*args)
    self.realSortedWalls = []
    self.currentSortingIndex = 0
    self.level = 0
    self.levelSaver = 0
    self.levelChangeStart = 0
    
  def Sort(self, currentGrid, gridSize, currentPastGrids, currentPastGridsIndex):
    #create the array of wall hights
    wallHeights = super().Sort(currentGrid)

    #this will be the main wall array that the UI will refrence
    for i in range(len(wallHeights)):
      indexToArray = []
      indexToArray.append(wallHeights[i])
      self.realSortedWalls.append(indexToArray)

    print("real sorted walls:", self.realSortedWalls)

    #STEP 1 :enter the sort
    sortedWalls = self.MergeSort(wallHeights, currentGrid)
    print(sortedWalls)

  def MergeSort(self, wallHeights, currentGrid):
    #splitting the array in half
    newWallHeights = [[], []]

    #STEP 2.5: if the array cannot be halved anymore, return and don't recurse anymore
    if len(wallHeights) == 1:
      self.level += 1
      return wallHeights

    #STEP 2: half up the arrays
    #height numbers from start to half
    for index in range(ceil(len(wallHeights)/2)):
      newWallHeights[0].append(wallHeights[index])
    #height numbers from half to end
    for index in range(ceil(len(wallHeights)/2), len(wallHeights)):
      newWallHeights[1].append(wallHeights[index])
    
    print("new wallHeights list split up:", newWallHeights)
    print("1st half:", newWallHeights[0])
    print("2nd half:", newWallHeights[1])

    #STEP 3: going up a level when entering a state of recursion
    self.level += 1
    print("recursion depth level:", self.level)
    

    #STEP 4: recursion for first half
    newWallHeights[0] = self.MergeSort(newWallHeights[0], currentGrid)
    print("firstHalf recursion done")
    #exiting recursion drops a level
    self.level -= 1
    
    #STEP 5: recursion for second half
    newWallHeights[1] = self.MergeSort(newWallHeights[1], currentGrid)
    print("secondHalf recursion done")
    #exiting recursion drops a level
    self.level -= 1

    

    
    #STEP 6: merge sort first half and second half then return array
    return self.Merge(newWallHeights[0], newWallHeights[1], currentGrid)

  def Merge(self, firstHalf, secondHalf, currentGrid):
    sortedArray = []

    #STEP 1: compare the first index of the two arrays. whatever is smaller gets appended to the sorted array
    while firstHalf and secondHalf:
      if firstHalf[0] > secondHalf[0]:
        sortedArray.append(secondHalf[0])
        secondHalf.pop(0)
      else:
        sortedArray.append(firstHalf[0])
        firstHalf.pop(0)
      
      

    #STEP 2: send the rest of the indexes to the sorted array
    while firstHalf:
      sortedArray.append(firstHalf[0]) 
      firstHalf.pop(0)

    while secondHalf:
      sortedArray.append(secondHalf[0])  
      secondHalf.pop(0)

    
    #STEP 3: conditionals for organizing the sorted list that the UI will read

    #new way-------------------------------------------------

    for i in range(len(self.realSortedWalls)):
      print("hi")



    #old way-------------------------------------------------

    # if len(self.realSortedWalls) == 2:
    #   self.realSortedWalls[0] = sortedArray
    #   self.realSortedWalls.pop(1)
    
    # elif self.level == self.levelSaver and self.currentSortingIndex < len(self.realSortedWalls) - 1:
    #   print(00000, "level:", self.level, self.levelSaver)
    #   self.realSortedWalls[self.currentSortingIndex] = sortedArray
    #   self.realSortedWalls.pop(self.currentSortingIndex + 1)
    #   self.currentSortingIndex += 1

    
      
    # elif self.level == self.levelSaver and self.currentSortingIndex >= len(self.realSortedWalls) - 1:
    #   print(11111, "level:", self.level, self.levelSaver)
    #   print("index:", self.currentSortingIndex)
    #   self.realSortedWalls[self.currentSortingIndex] = sortedArray
    #   self.currentSortingIndex += 1
      
    # elif self.level == self.levelSaver + 1 and len(sortedArray) == 2:
    #   print(2222, "level:", self.level, self.levelSaver)
    #   print("goin under")
    #   self.realSortedWalls[self.levelChangeStart - 1] = sortedArray
    #   self.realSortedWalls.pop(self.levelChangeStart)
    #   self.levelSaver = self.level
    #   print("currentSortingIndex:", self.currentSortingIndex, "levelChangeStart:", self.levelChangeStart)

    # elif self.level == self.levelSaver + 1 and len(sortedArray) == 3:
    #   print(2222.5, "level:", self.level, self.levelSaver)
    #   print("goin under")
    #   self.realSortedWalls[self.levelChangeStart] = sortedArray
    #   self.realSortedWalls.pop(self.levelChangeStart + 1)
    #   self.levelSaver = self.level
    #   print("currentSortingIndex:", self.currentSortingIndex, "levelChangeStart:", self.levelChangeStart)
      
    # elif self.level == self.levelSaver - 1 and self.currentSortingIndex < len(self.realSortedWalls) - 1 and len(sortedArray) == 3:
    #   print(33333.5, "level:", self.level, self.levelSaver)
    #   self.realSortedWalls[self.levelChangeStart - 1] = sortedArray
    #   self.realSortedWalls.pop(self.levelChangeStart)
    #   self.levelSaver = self.level
    #   self.levelChangeStart += 1
    #   self.currentSortingIndex += 1
    #   print("currentSortingIndex:", self.currentSortingIndex, "levelChangeStart:", self.levelChangeStart)

    # elif self.level == self.levelSaver - 1 and self.currentSortingIndex < len(self.realSortedWalls) - 1 and len(sortedArray) % 2 == 0 and len(sortedArray) != len(self.realSortedWalls) - 1:
    #   print(33333, "level:", self.level, self.levelSaver)
    #   self.realSortedWalls[self.levelChangeStart - 1] = sortedArray
    #   self.realSortedWalls.pop(self.levelChangeStart)
    #   self.levelChangeStart += 1
      
    #   self.levelSaver = self.level
    #   print("currentSortingIndex:", self.currentSortingIndex, "levelChangeStart:", self.levelChangeStart)

    # elif self.level == self.levelSaver - 1 and self.currentSortingIndex == len(self.realSortedWalls):
    #   print(55555, "level:", self.level, self.levelSaver)
    #   print("levelStartChanger:", self.levelChangeStart)
    #   self.realSortedWalls[1] = sortedArray
    #   self.currentSortingIndex = 0
    #   self.currentSortingIndex += 1
    #   self.realSortedWalls.pop(2)
    #   self.levelSaver = self.level
    #   self.levelChangeStart += 1
    #   print("currentSortingIndex:", self.currentSortingIndex, "levelChangeStart:", self.levelChangeStart)

    # elif self.level == self.levelSaver - 1 and len(sortedArray) == len(self.realSortedWalls) - 1 or self.level == self.levelSaver - 1 and len(sortedArray) == len(self.realSortedWalls) - 2:
    #   print(55555.5, "level:", self.level, self.levelSaver)
    #   print("levelStartChanger:", self.levelChangeStart)
    #   self.realSortedWalls[0] = sortedArray
    #   self.currentSortingIndex = 0
    #   self.realSortedWalls.pop(1)
    #   self.currentSortingIndex += 1
    #   self.levelSaver = self.level
    #   self.levelChangeStart = 1
    #   print("currentSortingIndex:", self.currentSortingIndex, "levelChangeStart:", self.levelChangeStart)
      
    # else:
    #   print(44444, "level:", self.level, self.levelSaver)
    #   print("levelStartChanger:", self.levelChangeStart)
    #   self.realSortedWalls[self.levelChangeStart] = sortedArray
    #   self.currentSortingIndex = 0
    #   self.realSortedWalls.pop(self.levelChangeStart + 1)
    #   self.currentSortingIndex += 1
    #   self.levelSaver = self.level
    #   self.levelChangeStart += 1
    #   print("currentSortingIndex:", self.currentSortingIndex, "levelChangeStart:", self.levelChangeStart)
      
    


    print("WHOLE currentWalls:", self.realSortedWalls)
        
    


    self.UpdateUI(currentGrid)
    print("sorted:", sortedArray)
    return sortedArray

  def UpdateUI(self, currentGrid):
    UIwallHeights = []
    clock = pygame.time.Clock()
    #STEP 1: loop through the 2D array to append all the heights into a 1D array
    for splitGroup in self.realSortedWalls:
      if isinstance(splitGroup, list):
        for wallHeight in splitGroup:
          UIwallHeights.append(wallHeight)
      else:
        UIwallHeights.append(splitGroup)

    #STEP 2: in the real grid, update the UI heights based on the UIwallHeights array (walls will be upside down)
    for gridRow in range(len(currentGrid)):
      for square in range(len(currentGrid[gridRow])):
        heightNumber = UIwallHeights[square]
        if gridRow < heightNumber:
          currentGrid[gridRow][square] = go.WALL
        else:
          currentGrid[gridRow][square] = go.NOTHING

    #STEP 3: flip the walls to right side up
    self.Gravity(currentGrid)
    

    #STEP 4: update UI with pygame
    for event in pygame.event.get():      
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    pygame.display.update()
    clock.tick(5)


  def Gravity(self, currentGrid):

    #STEP 1: while the scan has not been completed, move each square down if there is a space under it
    while True:
      scanComplete = True
      for gridRow in range(len(currentGrid) - 1):
        for square in range(len(currentGrid[gridRow])):
          
          #if current gridSquare is a wall and there is nothing below it and it is not at the bottom of the grid yet, move the square down and update the UI
          if currentGrid[gridRow + 1][square] == go.NOTHING and currentGrid[gridRow][square] == go.WALL and gridRow + 1 != -1:
            currentGrid[gridRow][square] = go.NOTHING
            currentGrid[gridRow + 1][square] = go.WALL
            self.viewManager.modelManager.gridMetaData.ChangeGridData(currentGrid, False, False, False)
            self.viewManager.uiGrid.Draw(currentGrid, [], 0, 0, go.NOTHING, None)
            scanComplete = False
      
      if scanComplete == True:
        break
          