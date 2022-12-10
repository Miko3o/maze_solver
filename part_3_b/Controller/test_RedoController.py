import pytest
from unittest.mock import MagicMock, patch
from Controller.RedoController import RedoController

@pytest.mark.xfail
def OlderGridIsReturned_When_UndoCalled():
  #setup
  redoController = RedoController()
  N = "nothing"
  W = "wall"
  pastGridsQuantity = 3
  numberOfUndos = 1
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
  pastGrids = [[
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
  currentGrid = redoController.Redo()

  #assert
  assert currentGrid == [
                        [W, W, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                                                ]