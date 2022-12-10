import pytest
from unittest.mock import MagicMock, patch
from Controller.GridController import GridController


#ResizeGrid-------------------------------------------

@pytest.mark.xfail
def test_GridIsResized_When_ResizeGridCalled():
  #setup
  gridController = GridController()
  N = "none"
  currentGrid = [
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                                        ]

  #work
  currentGrid = gridController.ResizeGrid(9, 9)

  
  #assert
  assert currentGrid == [
                        [N, N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N, N],
                                                  ]