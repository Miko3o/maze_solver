import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from Controller.Strategies.SolveMazeBFS import SolveMazeBFS
from View.GameStateENUM import GridObjects as go

#Solve--------------------------------------------

#note: later, account for the squares that would be filled as the algorithm's progress


class Test_SolveMazeBFS(unittest.TestCase):

  def test_MazePathMade_When_SolveCalled(self):
    #setup


    solveMazeBFS = SolveMazeBFS()
    N = go.NOTHING
    W = go.WALL
    S = go.SOLVER
    G = go.GOAL
    P = go.PATH
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
    currentGrid = solveMazeBFS.Solve(currentGrid, [], [])


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

if __name__ == "__main__":
  unittest.main()