import pytest
from unittest.mock import MagicMock, patch
from Controller.Strategies.SolveMazeAstar import SolveMazeAstar

#Solve--------------------------------------------

#note: later, account for the squares that would be filled as the algorithm's progress


@pytest.mark.xfail
def MazePathMade_When_SolveCalled():
  #setup
  solveMazeAstar = SolveMazeAstar()
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
  currentGrid = solveMazeAstar.Solve()


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

