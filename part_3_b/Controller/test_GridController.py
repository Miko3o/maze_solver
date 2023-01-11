import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from Controller.GridController import GridController
from View.GameStateENUM import GridObjects as go

#ResizeGrid-------------------------------------------

class Test_GridController(unittest.TestCase):
  def test_GridIsResized_When_ResizeGridCalled(self):
    #SETUP--------------------------------------
    gridController = GridController()
    N = go.NOTHING
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
    sliderX = 510
    gridSize = 8

    #WORK------------------------------------
    gridController.ResizeGrid(sliderX, currentGrid, gridSize)

    
    #ASSERT-----------------------------------
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
    

if __name__ == "__main__":
  unittest.main()
