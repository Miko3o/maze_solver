import Model.ModelManager
import View.ViewManager

from Controller.GravityController import GravityController
from Controller.GridController import GridController
from Controller.LoadMazeController import LoadMazeController
from Controller.NewMazeController import  NewMazeController
from Controller.RedoController import RedoController
from Controller.SaveMazeController import SaveMazeController
from Controller.SolveMazeController import SolveMazeController
from Controller.SortWallsController import SortWallsController
from Controller.UndoController import UndoController


class ControllerManager():

  def __init__(self):
    self.modelManager = Model.ModelManager.ModelManager
    self.viewManager = View.ViewManager.ViewManager
    
    self.gravityController = GravityController(self)
    self.gridController = GridController(self)
    self.loadMazeController = LoadMazeController(self)
    self.newMazeController = NewMazeController(self)
    self.redoController = RedoController(self)
    self.saveMazeController = SaveMazeController(self)
    self.solveMazeController = SolveMazeController(self)
    self.sortWallsController = SortWallsController(self)
    self.undoController = UndoController(self)

  def Sort(self):
    print("wip")