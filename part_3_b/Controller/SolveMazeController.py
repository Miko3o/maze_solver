from View.GameStateENUM import SolvingAlgorithm as sa


class SolveMazeController():

  def __init__(self, controllerManager, viewManager):
    self.controllerManager = controllerManager
    self.viewManager = viewManager
    self.solvingAlgorithm = sa.BFS

  def SetData(self):
    print("wip")

  def Solve(self, currentGrid, currentPastGrids, currentPastGridsIndex):
    if self.solvingAlgorithm == sa.BFS:
      self.controllerManager.solveMazeBFS.Solve(currentGrid, currentPastGrids, currentPastGridsIndex)
    elif self.solvingAlgorithm == sa.DFS:
      self.controllerManager.solveMazeDFS.Solve(currentGrid, currentPastGrids, currentPastGridsIndex)
    elif self.solvingAlgorithm == sa.Dijkstra:
      self.controllerManager.solveMazeDijkstra.Solve(currentGrid, currentPastGrids, currentPastGridsIndex)
    elif self.solvingAlgorithm == sa.Astar:
      self.controllerManager.solveMazeAstar.Solve(currentGrid, currentPastGrids, currentPastGridsIndex)


  def ChangeStrategy(self, newStrategy):
    self.solvingAlgorithm = newStrategy
    print("newStrategy:", self.solvingAlgorithm)

  def GetAllStrategies(self):
    print("wip")
