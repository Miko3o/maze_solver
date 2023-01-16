import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from Controller.SolveMazeController import SolveMazeController
from View.GameStateENUM import GridObjects as go, SolvingAlgorithm as sa



#Solve--------------------------------------------




class Test_SolveMazeController(unittest.TestCase):
  def test_MazeSolvedUsingBFS_When_SolveMazeControllerCalled(self):
    #SETUP-------------------------------------------------
    #mock args
    mock_controllerManager = Mock()
    mock_viewManager = Mock()

    solveMazeController = SolveMazeController(mock_controllerManager, mock_viewManager)
    N = go.NOTHING
    W = go.WALL
    S = go.SOLVER
    G = go.GOAL
    P = go.PATH
    F = go.FINDER
    currentGrid = [
                  [N, N, N, N, W, N, N, N],
                  [N, S, W, N, W, N, W, N],
                  [N, W, N, N, W, N, W, N],
                  [N, W, N, W, W, N, W, N],
                  [N, W, N, N, N, N, W, N],
                  [N, W, W, N, W, W, N, N],
                  [N, W, N, N, W, W, N, W],
                  [W, N, N, W, W, G, N, W],
                                          ]
    solveMazeController.solvingAlgorithm = sa.BFS
    currentPastGrids = []
    currentPastGridsIndex = 0

    #WORK-----------------------------------
    solveMazeController.Solve(currentGrid, currentPastGrids, currentPastGridsIndex)


    #ASSERT--------------------------------
    solveMazeController.controllerManager.solveMazeBFS.Solve.assert_called

  def test_MazeSolvedUsingDFS_When_SolveMazeControllerCalled(self):
    #SETUP-------------------------------------------------
    #mock args
    mock_controllerManager = Mock()
    mock_viewManager = Mock()

    solveMazeController = SolveMazeController(mock_controllerManager, mock_viewManager)
    N = go.NOTHING
    W = go.WALL
    S = go.SOLVER
    G = go.GOAL
    P = go.PATH
    F = go.FINDER
    currentGrid = [
                  [N, N, N, N, W, N, N, N],
                  [N, S, W, N, W, N, W, N],
                  [N, W, N, N, W, N, W, N],
                  [N, W, N, W, W, N, W, N],
                  [N, W, N, N, N, N, W, N],
                  [N, W, W, N, W, W, N, N],
                  [N, W, N, N, W, W, N, W],
                  [W, N, N, W, W, G, N, W],
                                          ]
    solveMazeController.solvingAlgorithm = sa.BFS
    currentPastGrids = []
    currentPastGridsIndex = 0

    #WORK-----------------------------------
    solveMazeController.Solve(currentGrid, currentPastGrids, currentPastGridsIndex)


    #ASSERT--------------------------------
    solveMazeController.controllerManager.solveMazeDFS.Solve.assert_called

  def test_MazeSolvedUsingDijkstra_When_SolveMazeControllerCalled(self):
    #SETUP-------------------------------------------------
    #mock args
    mock_controllerManager = Mock()
    mock_viewManager = Mock()

    solveMazeController = SolveMazeController(mock_controllerManager, mock_viewManager)
    N = go.NOTHING
    W = go.WALL
    S = go.SOLVER
    G = go.GOAL
    P = go.PATH
    F = go.FINDER
    currentGrid = [
                  [N, N, N, N, W, N, N, N],
                  [N, S, W, N, W, N, W, N],
                  [N, W, N, N, W, N, W, N],
                  [N, W, N, W, W, N, W, N],
                  [N, W, N, N, N, N, W, N],
                  [N, W, W, N, W, W, N, N],
                  [N, W, N, N, W, W, N, W],
                  [W, N, N, W, W, G, N, W],
                                          ]
    solveMazeController.solvingAlgorithm = sa.BFS
    currentPastGrids = []
    currentPastGridsIndex = 0

    #WORK-----------------------------------
    solveMazeController.Solve(currentGrid, currentPastGrids, currentPastGridsIndex)


    #ASSERT--------------------------------
    solveMazeController.controllerManager.solveMazeDijkstra.Solve.assert_called

  def test_MazeSolvedUsingAstar_When_SolveMazeControllerCalled(self):
    #SETUP-------------------------------------------------
    #mock args
    mock_controllerManager = Mock()
    mock_viewManager = Mock()

    solveMazeController = SolveMazeController(mock_controllerManager, mock_viewManager)
    N = go.NOTHING
    W = go.WALL
    S = go.SOLVER
    G = go.GOAL
    P = go.PATH
    F = go.FINDER
    currentGrid = [
                  [N, N, N, N, W, N, N, N],
                  [N, S, W, N, W, N, W, N],
                  [N, W, N, N, W, N, W, N],
                  [N, W, N, W, W, N, W, N],
                  [N, W, N, N, N, N, W, N],
                  [N, W, W, N, W, W, N, N],
                  [N, W, N, N, W, W, N, W],
                  [W, N, N, W, W, G, N, W],
                                          ]
    solveMazeController.solvingAlgorithm = sa.BFS
    currentPastGrids = []
    currentPastGridsIndex = 0

    #WORK-----------------------------------
    solveMazeController.Solve(currentGrid, currentPastGrids, currentPastGridsIndex)


    #ASSERT--------------------------------
    solveMazeController.controllerManager.solveMazeAstar.Solve.assert_called




  #ChangeStrategy--------------------------------------
  def test_StrategyIsChangedToDFS_When_ChangeStrategiesCalled(self):
    #SETUP-------------------------------------------------
    #mock args
    mock_controllerManager = Mock()
    mock_viewManager = Mock()

    solveMazeController = SolveMazeController(mock_controllerManager, mock_viewManager)
    solveMazeController.solvingAlgorithm = sa.BFS
    newStrategy = sa.DFS

    #WORK----------------------------------
    solveMazeController.ChangeStrategy(newStrategy)

    #ASSERT----------------------------------
    assert solveMazeController.solvingAlgorithm == sa.DFS

if __name__ == "__main__":
  unittest.main()