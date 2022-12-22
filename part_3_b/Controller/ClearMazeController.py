from View.GameStateENUM import GridObjects as go


class ClearMazeController():

  def __init__(self, viewManager):
    self.viewManager = viewManager

  def ClearMaze(self, currentGrid):
    for gridRow in range(len(currentGrid)):
      for square in range(len(currentGrid[gridRow])):
        if currentGrid[gridRow][square] != go.NOTHING:
          currentGrid[gridRow][square] = go.NOTHING
    self.viewManager.modelManager.gridMetaData.ChangeGridData(currentGrid, False, False, False)