


class UndoController():

  def __init__(self, viewManager):
    self.viewManager = viewManager

  def Undo(self, currentGrid, currentGridSize, currentPastGrids, currentPastGridsIndex):
    realIndex = self.ConvertIndexToPositiveNumberHandler(currentPastGrids, currentPastGridsIndex)
    print("CPG:", len(currentPastGrids))
    print("CPGI:", currentPastGridsIndex)
    print("realIndex:", realIndex)
    if realIndex !=0:

      #set the current grid to the previous grid in the past grids list and set the current index 1 below
      print("currentGrid length1:", len(currentGrid))
      currentGrid = currentPastGrids[currentPastGridsIndex - 1]
      currentPastGridsIndex -= 1

      #set the grid size to the size of the past grid
      print("current index:", currentPastGridsIndex)
      currentGridSize = len(currentGrid[0])
      print("currentGridSize:", currentGridSize)

      #change grid data
      self.viewManager.modelManager.gridMetaData.ChangeGridData(currentGrid, currentGridSize, currentPastGrids, currentPastGridsIndex)
      print("pastGrid length:", len(currentPastGrids))


  def ConvertIndexToPositiveNumberHandler(self, currentPastGrids, currentPastGridsIndex):
    indexItem = currentPastGrids[currentPastGridsIndex]
    print("pastGrids index:", currentPastGrids.index(indexItem))
    return currentPastGrids.index(indexItem)