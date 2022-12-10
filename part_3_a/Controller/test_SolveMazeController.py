import pytest
from unittest.mock import MagicMock, patch
from Controller.SolveMazeController import SolveMazeController


#SetData-----------*INCOMPLETE*-------------------

#note: what is this?????

@pytest.mark.xfail
def test_DataIsSet_When_SetDataCalled():
  print("wip")


#Solve--------------------------------------------

#note: later, account for the squares that would be filled as the algorithm's progress


@pytest.mark.xfail
def MazePathMade_When_SolveCalled():
  #setup
  solveMazeController = SolveMazeController()
  N = "nothing"
  W = "wall"
  S = "solver"
  G = "goal"
  P = "path"
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

  #work
  currentGrid = solveMazeController.Solve()


  #assert
  assert currentGrid == [
                        [N, P, P, P, W, P, P, P],
                        [N, S, W, P, W, P, W, P],
                        [N, W, P, P, W, P, W, P],
                        [N, W, P, W, W, P, W, P],
                        [N, W, P, P, P, P, W, P],
                        [N, W, W, N, W, W, P, P],
                        [N, W, N, N, W, W, P, W],
                        [W, N, N, W, W, G, P, W],
                                               ]

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