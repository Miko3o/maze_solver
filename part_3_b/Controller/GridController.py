from math import floor
from View.GameStateENUM import GridObjects as go

class GridController():

  def __init__(self):
    self.sliderX = 507

  def ResizeGrid(self, sliderX, currentGrid, gridSize):
    percentSlided = ((sliderX - 464)/91)
    newGridSize = floor(4 + (10*(percentSlided)))
    #if slider was not slided
    sizeDifference = abs(newGridSize - gridSize)
    
    if gridSize == newGridSize:
      return currentGrid, gridSize
      
    #if slider is slided to the right
    elif gridSize < newGridSize:
      for i in range(sizeDifference):
        #increase grid width
        newArray = []
        for n in range(len(currentGrid)):
          currentGrid[n].append(go.NOTHING)
          newArray.append(go.NOTHING)
        #increase grid hieght
        currentGrid.append(newArray)
      gridSize = newGridSize
      return currentGrid, gridSize
      
    #if slider is slided to the left
    elif gridSize > newGridSize:
      for i in range(sizeDifference):
        #decrease grid width
        for n in range(len(currentGrid)):
          currentGrid[n].pop()
        #decrease grid hieght
        currentGrid.pop()
      gridSize = newGridSize
      return currentGrid, gridSize