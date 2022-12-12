import Model.ModelManager
import View.ViewManager

from Controller.GravityController import GravityController
from Controller.GridController import GridController
from Controller.GridObjectController import GridObjectController
from Controller.LoadMazeController import LoadMazeController
from Controller.NewMazeController import  NewMazeController
from Controller.RedoController import RedoController
from Controller.SaveMazeController import SaveMazeController
from Controller.SolveMazeController import SolveMazeController
from Controller.SortWallsController import SortWallsController
from Controller.UndoController import UndoController


class ControllerManager():

  def __init__(self, viewManager):
    self.modelManager = Model.ModelManager.ModelManager
    self.viewManager = View.ViewManager.ViewManager
    
    self.gravityController = GravityController()
    self.gridController = GridController()
    self.gridObjectController = GridObjectController(viewManager)
    self.loadMazeController = LoadMazeController(viewManager)
    self.newMazeController = NewMazeController()
    self.redoController = RedoController(viewManager)
    self.saveMazeController = SaveMazeController()
    self.solveMazeController = SolveMazeController()
    self.sortWallsController = SortWallsController()
    self.undoController = UndoController(viewManager)

  def Sort(self):
    print("Sort: wip")