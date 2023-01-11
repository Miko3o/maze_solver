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

if __name__ == "__main__":
  unittest.main()


#ChangeStrategy--------------------------------------

@pytest.mark.xfail
def StrategyIsChanged_When_ChangeStrategiesCalled():
  #setup
  solveMazeController = SolveMazeController()
  currentStrategy = "BFS"

  #work
  currentStrategy = solveMazeController.ChangeStrategy

  #assert
  assert currentStrategy == "DFS"


#GetAllStrategies-------*INCOMPLETE*-----(displays on the dropdown)

@pytest.mark.xfail
def StrategiesAreDisplayed_When_GetAllStrategiesCalled():

  #note: also forgot what this does
  
  #setup
  solveMazeController = SolveMazeController()
  print("wip")