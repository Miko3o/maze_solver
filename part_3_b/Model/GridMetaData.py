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
    self.pastGrids = [[
                       [N, N, N, N, N, N, N, N],
                       [N, N, N, N, N, N, N, N],
                       [N, N, N, N, N, N, N, N],
                       [N, N, N, N, N, N, N, N],
                       [N, N, N, N, N, N, N, N],
                       [N, N, N, N, N, N, N, N],
                       [N, N, N, N, N, N, N, N],
                       [N, N, N, N, N, N, N, N]
                                               ]]

    self.gridSize = 8

    self.currentPastGridsIndex = -1
    
    #Exist Conditions
    self.solverExists = False
    self.goalExists = False
  
  def GetGridData(self):
    return self.currentGrid, self.gridSize, self.pastGrids, self.currentPastGridsIndex
    
  def ChangeGridData(self, newGrid, newGridSize, newPastGrids, currentPastGridsIndex):
    self.currentGrid = newGrid
    if newGridSize !=False:
      self.gridSize = newGridSize
    if newPastGrids !=False:
      self.pastGrids = newPastGrids
    if currentPastGridsIndex != False:
      self.currentPastGridsIndex = currentPastGridsIndex
    

      
