from Model.GoalMetaData import GoalMetaData
from Model.GridMetaData import GridMetaData
from Model.SolverMetaData import SolverMetaData
from Model.WallMetaData import WallMetaData


class ModelManager():

  def __init__(self, N, W, S, G, F, P):
    self.goalMetadata = GoalMetaData()
    self.gridMetaData = GridMetaData(N, W, S, G, F, P)
    self.sovlerMetaData = SolverMetaData()
    self.wallMetaData = WallMetaData()
