import copy


class RedoController():

  def __init__(self, viewManager):
    self.viewManager = viewManager

  def Redo(self, currentGrid, gridSize, currentPastGrids, currentPastGridsIndex):

    if currentPastGridsIndex != -1:
      #set the current grid to the next grid in the past grids list and set the current index 1 above
      print("currentGrid length1:", len(currentGrid))
      currentGrid = copy.deepcopy(currentPastGrids[currentPastGridsIndex + 1])
      currentPastGridsIndex += 1

      #set the grid size to the size of the past grid
      print("current index:", currentPastGridsIndex)
      currentGridSize = len(currentGrid[0])
      print("currentGridSize:", currentGridSize)


      #change grid data
      self.viewManager.modelManager.gridMetaData.ChangeGridData(currentGrid, currentGridSize, currentPastGrids, currentPastGridsIndex)
      print("pastGrid length:", len(currentPastGrids))