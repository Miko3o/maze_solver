import copy


class UndoController():

  def __init__(self, viewManager):
    self.viewManager = viewManager

  def Undo(self, currentGrid, currentGridSize, currentPastGrids, currentPastGridsIndex):
    #STEP 1: get the actual index
    realIndex = self.ConvertIndexToPositiveNumberHandler(currentPastGrids, currentPastGridsIndex)
    
    print("realIndex:", realIndex)
    if realIndex !=0:

      #STEP 2: set the current grid to the previous grid in the past grids list and set the current index 1 below
      currentGrid = copy.deepcopy(currentPastGrids[realIndex - 1])
      currentPastGridsIndex -= 1

      ##STEP 3: set the grid size to the size of the past grid
      currentGridSize = len(currentGrid[0])
      

      #STEP 4: change grid data
      self.viewManager.modelManager.gridMetaData.ChangeGridData(currentGrid, currentGridSize, currentPastGrids, currentPastGridsIndex)
      print("CPG length:", len(currentPastGrids))
      print("CPGI:", currentPastGridsIndex)


  def ConvertIndexToPositiveNumberHandler(self, currentPastGrids, currentPastGridsIndex):
    positiveIndex = currentPastGridsIndex % len(currentPastGrids)
    return positiveIndex