


class UndoController():

  def __init__(self, viewManager):
    self.viewManager = viewManager
    self.currentPastGridsIndex = 0
    self.currentGrid = []

  def Undo(self, currentGrid, currentGridSize, currentPastGrids):
    print("currentGrid length1:", len(self.currentGrid))
    self.currentGrid = currentPastGrids[self.currentPastGridsIndex - 1]
    print("currentGrid length2:", len(self.currentGrid))
    self.currentPastGridsIndex -= 1
    print("current index:", self.currentPastGridsIndex)
    currentGridSize = len(self.currentGrid[0])
    print("currentGridSize:", currentGridSize)
    self.viewManager.modelManager.gridMetaData.ChangeGridData(self.currentGrid, currentGridSize, currentPastGrids)
    print("pastGrid length:", len(currentPastGrids))


