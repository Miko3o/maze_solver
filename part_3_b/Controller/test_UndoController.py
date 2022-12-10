import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from Controller.UndoController import UndoController

class Test_UndoController(unittest.TestCase):


  def test_OlderGridIsReturned_When_UndoCalled(self):
    #setup
    viewManager = Mock()
    undoController = UndoController(viewManager)
    N = "nothing"
    W = "wall"
    pastGridsQuantity = 3
    currentGrid = [
                  [W, W, W, W, W, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                                          ]
    currentPastGrids = [[
                  [W, W, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                                          ],
                [
                  [W, W, W, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                                          ],
                [
                  [W, W, W, W, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                                          ]]

    #work
    newGrid = undoController.Undo(currentGrid, 8, currentPastGrids)
    print("newGrid:", newGrid)
    #assert
    assert newGrid == currentPastGrids[pastGridsQuantity - 1]

if __name__ == "__main__":
  unittest.main()