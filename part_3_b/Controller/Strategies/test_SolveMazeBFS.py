import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from Controller.Strategies.SolveMazeBFS import SolveMazeBFS
from View.GameStateENUM import GridObjects as go

#Solve--------------------------------------------

#note: later, account for the squares that would be filled as the algorithm's progress


class Test_SolveMazeBFS(unittest.TestCase):
  @patch("pygame.draw.rect")
  @patch("pygame.display.update")
  @patch("pygame.event.get")
  def test_MazePathMade_When_SolveCalled(self, mock_pygameEventGet, mock_pygameDisplayUpdate, mock_pygameDrawRect):
    #SETUP--------------------------------
    #mocking arg objects
    mock_viewManager = Mock()
    mock_gameWindow = Mock()

    #mock function return value
    mock_pygameEventGet.return_value = []
    mock_pygameDisplayUpdate.return_value = "hi"
    mock_pygameDrawRect.return_value = "hi"


    solveMazeBFS = SolveMazeBFS(mock_viewManager, mock_gameWindow)
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

    #WORK------------------------------------------------
    solveMazeBFS.Solve(currentGrid, [], 0)


    #ASSERT-------------------------------------------------
    assert currentGrid == [
                          [F, P, P, P, W, P, P, P],
                          [F, S, W, P, W, P, W, P],
                          [F, W, P, P, W, P, W, P],
                          [F, W, P, W, W, P, W, P],
                          [F, W, P, P, P, P, W, P],
                          [F, W, W, F, W, W, P, P],
                          [F, W, F, F, W, W, P, W],
                          [W, F, F, W, W, G, P, W],
                                                  ]


  #GetSolverLocation----------------------------------------------
  def test_SolverLocationIsFound_When_GetSolverLocationCalled(self):
    #SETUP----------------------------------------
    #mocking arg objects
    mock_viewManager = Mock()
    mock_gameWindow = Mock()

    solveMazeBFS = SolveMazeBFS(mock_viewManager, mock_gameWindow)

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

    #WORK-------------------------------------------
    solverLocation = solveMazeBFS.GetSolverLocation(currentGrid)


    #ASSERT-----------------------------------------
    assert solverLocation == (1, 1)

if __name__ == "__main__":
  unittest.main()