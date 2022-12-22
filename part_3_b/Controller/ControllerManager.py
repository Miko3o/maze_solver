import Model.ModelManager
import View.ViewManager

from Controller.ClearMazeController import ClearMazeController
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

from Controller.Strategies.BubbleSort import BubbleSort
from Controller.Strategies.IntersectionSort import IntersectionSort
from Controller.Strategies.MergeSort import MergeSort
from Controller.Strategies.QuickSort import QuickSort
from Controller.Strategies.RadixSort import RadixSort
from Controller.Strategies.SelectionSort import SelectionSort
from Controller.Strategies.SolveMazeAstar import SolveMazeAstar
from Controller.Strategies.SolveMazeBFS import SolveMazeBFS
from Controller.Strategies.SolveMazeDFS import SolveMazeDFS
from Controller.Strategies.SolveMazeDijkstra import SolveMazeDijkstra


class ControllerManager():

  def __init__(self, viewManager, gameWindow):
    self.modelManager = Model.ModelManager.ModelManager
    self.viewManager = View.ViewManager.ViewManager

    #Controllers
    self.clearMazeController = ClearMazeController(viewManager)
    self.gravityController = GravityController(viewManager)
    self.gridController = GridController()
    self.gridObjectController = GridObjectController(viewManager)
    self.loadMazeController = LoadMazeController(viewManager)
    self.newMazeController = NewMazeController()
    self.redoController = RedoController(viewManager)
    self.saveMazeController = SaveMazeController()
    self.solveMazeController = SolveMazeController(self, viewManager)
    self.sortWallsController = SortWallsController()
    self.undoController = UndoController(viewManager)

    #Strategies
    self.bubbleSort = BubbleSort(viewManager, gameWindow)
    self.intersectionSort = IntersectionSort(viewManager, gameWindow)
    self.mergeSort = MergeSort(viewManager, gameWindow)
    self.quickSort = QuickSort(viewManager, gameWindow)
    self.radixSort = RadixSort(viewManager, gameWindow)
    self.selectionSort = SelectionSort(viewManager, gameWindow)
    self.solveMazeAstar = SolveMazeAstar(viewManager, gameWindow)
    self.solveMazeBFS = SolveMazeBFS(viewManager, gameWindow)
    self.solveMazeDFS = SolveMazeDFS(viewManager, gameWindow)
    self.solveMazeDijkstra = SolveMazeDijkstra(viewManager, gameWindow)

  def Sort(self):
    print("Sort: wip")