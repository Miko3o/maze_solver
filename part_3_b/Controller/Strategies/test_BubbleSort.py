import pytest
import pygame
import unittest
from View.GameStateENUM import GridObjects as go
from unittest.mock import MagicMock, patch, Mock
from Controller.Strategies.BubbleSort import BubbleSort
#from Controller.Strategies.mock_AbstractStrategy import mock_AbstractStrategy


#Sort--------------------------------------------
class Test_BubbleSort(unittest.TestCase):

  @patch("pygame.display.update")
  @patch("pygame.event.get")
  def test_UIIsUpdated_When_SortCalled(self, mock_pygameEventGet, mock_pygameDisplayUpdate):
    #SETUP-----------------------------------------------
    #pygame functions to be mocked
    mock_pygameEventGet.return_value = []
    mock_pygameDisplayUpdate.return_value = "hi"
    
    #arg classes to be mocked
    viewManager = Mock()
    gameWindow = Mock()

    #bubblesort object
    bubbleSort = BubbleSort(viewManager, gameWindow)

    #args to be passed into the sort method
    N = go.NOTHING
    W = go.WALL
    currentGrid = [
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, W, N, N, N],
                  [N, N, N, N, W, N, N, N],
                  [N, W, N, N, W, N, N, N],
                  [N, W, N, N, W, N, W, N],
                  [N, W, N, N, W, N, W, N],
                  [N, W, W, W, W, W, W, W],
                  [W, W, W, W, W, W, W, W],
                                          ]
    gridSize = 8
    currentPastGrids = []
    currentPastGridsIndex = 0



    #WORK--------------------------------------------
    bubbleSort.Sort(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)



    #ASSERT-------------------------------------------
    assert currentGrid == [
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, W],
                          [N, N, N, N, N, N, N, W],
                          [N, N, N, N, N, N, W, W],
                          [N, N, N, N, N, W, W, W],
                          [N, N, N, N, N, W, W, W],
                          [N, W, W, W, W, W, W, W],
                          [W, W, W, W, W, W, W, W],
                                                  ]


  #SwapIndexes------------------------------------------
  def test_WallHeightsIndexesAreSwapped_When_Called(self):
    #SETUP----------------------------------------------
    #arg classes to be mocked
    viewManager = Mock()
    gameWindow = Mock()

    #bubblesort object
    bubbleSort = BubbleSort(viewManager, gameWindow)

    #args to be passed into the swap method
    N = go.NOTHING
    W = go.WALL
    currentGrid = [
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, W, N, N, N],
                  [N, N, N, N, W, N, N, N],
                  [N, W, N, N, W, N, N, N],
                  [N, W, N, N, W, N, W, N],
                  [N, W, N, N, W, N, W, N],
                  [N, W, W, W, W, W, W, W],
                  [W, W, W, W, W, W, W, W],
                                          ]
    currentPastGrids = []
    wallHeights = [1, 5, 2, 2, 7, 2, 4, 2]

    #WORK----------------------------------------------
    bubbleSort.SwapIndexes(currentGrid, wallHeights, 1, currentPastGrids)

    #ASSERT--------------------------------------------
    assert wallHeights == [1, 2, 5, 2, 7, 2, 4, 2]

  def test_GridIndexesAreSwapped_When_Called(self):
    #SETUP----------------------------------------------
    #arg classes to be mocked
    viewManager = Mock()
    gameWindow = Mock()

    #bubblesort object
    bubbleSort = BubbleSort(viewManager, gameWindow)

    #args to be passed into the swap method
    N = go.NOTHING
    W = go.WALL
    currentGrid = [
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, W, N, N, N],
                  [N, N, N, N, W, N, N, N],
                  [N, W, N, N, W, N, N, N],
                  [N, W, N, N, W, N, W, N],
                  [N, W, N, N, W, N, W, N],
                  [N, W, W, W, W, W, W, W],
                  [W, W, W, W, W, W, W, W],
                                          ]
    currentPastGrids = []
    wallHeights = [1, 5, 2, 2, 7, 2, 4, 2]

    #WORK----------------------------------------------
    bubbleSort.SwapIndexes(currentGrid, wallHeights, 1, currentPastGrids)

    #ASSERT--------------------------------------------
    assert currentGrid == [
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, W, N, N, N],
                          [N, N, N, N, W, N, N, N],
                          [N, N, W, N, W, N, N, N],
                          [N, N, W, N, W, N, W, N],
                          [N, N, W, N, W, N, W, N],
                          [N, W, W, W, W, W, W, W],
                          [W, W, W, W, W, W, W, W],
                                                  ]


if __name__ == "__main__":
  unittest.main()