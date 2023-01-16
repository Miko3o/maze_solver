import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from Controller.GravityController import GravityController
from View.GameStateENUM import GridObjects as go


class Test_GravityController(unittest.TestCase):
  @patch("pygame.event.get")
  @patch("pygame.display.update")
  def test_BlocksAreFallen_When_GravityCOntrollerCalled(self, mock_pygameDisplayUpdate, mock_pygameEventGet):
    #SETUP-------------------------------------
    #mock functions
    mock_pygameDisplayUpdate.return_value = "hi"
    mock_pygameEventGet.return_value = []

    #mock args
    mock_viewManager = Mock()

    gravityController = GravityController(mock_viewManager)
    N = go.NOTHING
    W = go.WALL
    
    currentGrid = [
                  [W, N, N, N, N, N, W, N],
                  [W, N, N, N, N, N, N, N],
                  [N, N, N, N, W, N, N, N],
                  [N, N, N, N, N, N, W, N],
                  [N, N, N, N, W, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, W, N, N, N],
                  [N, N, N, N, N, N, N, N],
                                          ]

    #WORK--------------------------------------
    gravityController.Gravity(currentGrid)

    #ASSERT----------------------------------------
    assert currentGrid == [
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, W, N, N, N],
                          [W, N, N, N, W, N, W, N],
                          [W, N, N, N, W, N, W, N],
                                                  ]


if __name__ == "__main__":
  unittest.main()

