import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from Controller.Strategies.SolveMazeDFS import SolveMazeDFS
from View.GameStateENUM import GridObjects as go

#Solve--------------------------------------------

#note: later, account for the squares that would be filled as the algorithm's progress


class Test_SolveMazeDFS(unittest.TestCase):
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


    solveMazeDFS = SolveMazeDFS(mock_viewManager, mock_gameWindow)
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

    #work
    solveMazeDFS.Solve(currentGrid, [], 0)


    #assert
    assert currentGrid == [
                          [F, P, P, P, W, P, P, P],
                          [F, S, W, P, W, P, W, P],
                          [N, W, P, P, W, P, W, P],
                          [N, W, P, W, W, P, W, P],
                          [N, W, P, P, P, P, W, P],
                          [N, W, W, F, W, W, P, P],
                          [N, W, N, N, W, W, P, W],
                          [W, N, N, W, W, G, P, W],
                                                  ]

  #GetSolverLocation----------------------------------------------
  def test_SolverLocationIsFound_When_GetSolverLocationCalled(self):
    #SETUP----------------------------------------
    #mocking arg objects
    mock_viewManager = Mock()
    mock_gameWindow = Mock()

    solveMazeDFS = SolveMazeDFS(mock_viewManager, mock_gameWindow)

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
    solverLocation = solveMazeDFS.GetSolverLocation(currentGrid)


    #ASSERT-----------------------------------------
    assert solverLocation == (1, 1)

if __name__ == "__main__":
  unittest.main()