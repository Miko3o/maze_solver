from Model.GoalMetaData import GoalMetaData
from Model.GridMetaData import GridMetaData
from Model.SolverMetaData import SolverMetaData
from Model.WallMetaData import WallMetaData


class ModelManager():

  def __init__(self):
    self.goalMetadata = GoalMetaData(self)
    self.gridMetaData = GridMetaData(self)
    self.sovlerMetaData = SolverMetaData(self)
    self.wallMetaData = WallMetaData(self)
