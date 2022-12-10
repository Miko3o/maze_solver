from View.GameStateENUM import GridObjects as go


class GridMetaData():

  def __init__(self, N, W, S, G, F, P):
    self.currentGrid = [
                       [N, N, N, N, N, N, N, N],
                       [N, N, N, N, N, N, N, N],
                       [N, N, N, N, N, N, N, N],
                       [N, N, N, N, N, N, N, N],
                       [N, N, N, N, N, N, N, N],
                       [N, N, N, N, N, N, N, N],
                       [N, N, N, N, N, N, N, N],
                       [N, N, N, N, N, N, N, N]
                                               ]
    self.pastGrids = []

    self.gridSize = 8
    
    #Exist Conditions
    self.solverExists = False
    self.goalExists = False
  
  def GetGridData(self):
    return self.currentGrid, self.gridSize, self.pastGrids
    
  def ChangeGridData(self, newGrid, newGridSize, newPastGrids):
    self.currentGrid = newGrid
    if newGridSize !=False:
      self.gridSize = newGridSize
    if newPastGrids !=False:
      self.pastGrids = newPastGrids

      
