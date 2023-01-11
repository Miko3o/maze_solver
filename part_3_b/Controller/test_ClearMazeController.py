import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from Controller.ClearMazeController import ClearMazeController
from View.GameStateENUM import GridObjects as go


class Test_ClearMazeController(unittest.TestCase):
  def test_MazeIsCleared_When_NewMazeCalled(self):
    #SETUP---------------------------------
    #mocking args
    mock_viewManager = Mock()

    clearMazeController = ClearMazeController(mock_viewManager)
    N = go.NOTHING
    W = go.WALL
    currentGrid = [
                  [W, W, W, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                                          ]
    
    
    #WORK--------------------------------------
    clearMazeController.ClearMaze(currentGrid)

    #ASSERT-------------------------------------
    assert currentGrid == [
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                                                  ]


if __name__ == "__main__":
  unittest.main()

