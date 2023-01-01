from Controller.Strategies.AbstractStrategy import AbstractStrategy
from View.GameStateENUM import GridObjects as go
import pygame

class RadixSort(AbstractStrategy):

  def __init__(self, *args):
    super().__init__(*args)
    
  def Sort(self, currentGrid, gridSize, currentPastGrids, currentPastGridsIndex):
    wallHeights = super().Sort(currentGrid)

    #STEP 1: set maxDigit to the number of digits of the heighest height
    maxNumber = max(wallHeights)

    #STEP 2: do counting sort for every digit:
    place = 1
    while maxNumber//place >= 1:
      self.countingSort(wallHeights, place, currentGrid)
      place *= 10
      print("next digit:", wallHeights)

    print("finish:", wallHeights)

  def countingSort(self, wallHeights, place, currentGrid):

    #STEP 1: initialize arrays for keeping track of how many of each current place digit there is
    size = len(wallHeights)
    output = [0] * size
    count = [0] * 10

    print("output:", output)
    print("count:", count)

    #STEP 2: get the current place digit and put it in their corresponding index
    for i in range(0, size):
      index = wallHeights[i] // place
      count[index % 10] += 1
      print("index:", index)
      print("count:", count)

    #STEP 3: change count[i] so that it is the position of digit in ouput array
    print("NEXT STEP")
    for i in range(1, 10):
      count[i] += count[i - 1]
      print("COUNT:", count)

    #STEP 4: work backwards to build the output array
    i = size - 1
    print("NEXT STEP")
    while i >=0:
      index = wallHeights[i] // place
      output[count[index % 10] - 1] = wallHeights[i]
      count[index % 10] -= 1
      i -= 1
      print("index:", index)
      print("output:", output)
      print("count:", count)
      print("i:", i)
      

    #STEP 5:copy output to wallHeights array and updaate UI
    i = 0
    for i in range(0, len(wallHeights)):
      wallHeights[i] = output[i]
      self.UpdateUI(currentGrid, wallHeights)
    



  def UpdateUI(self, currentGrid, UIwallHeights):
    clock = pygame.time.Clock()

    #STEP 1: in the real grid, update the UI heights based on the UIwallHeights array (walls will be upside down)
    for gridRow in range(len(currentGrid)):
      for square in range(len(currentGrid[gridRow])):
        heightNumber = UIwallHeights[square]
        if gridRow < heightNumber:
          currentGrid[gridRow][square] = go.WALL
        else:
          currentGrid[gridRow][square] = go.NOTHING

    #STEP 2: flip the walls to right side up
    self.Gravity(currentGrid)
    

    #STEP 3: update UI with pygame
    for event in pygame.event.get():      
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    pygame.display.update()
    clock.tick(600)
    

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
          