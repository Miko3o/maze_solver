import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from Controller.Strategies.SelectionSort import SelectionSort
from View.GameStateENUM import GridObjects as go

#Sort--------------------------------------------

class Test_IntersectionSort(unittest.TestCase):
  @patch("pygame.display.update")
  @patch("pygame.event.get")
  def test_UIWallsAreSorted_When_SortCalled(self, mock_pygameEventGet, mock_pygameDisplayUpdate):
    #SETUP----------------------------------
    #mocking arg objects
    mock_viewManager = Mock()
    mock_gameWindow = Mock()

    #mock function return value
    mock_pygameEventGet.return_value = []
    mock_pygameDisplayUpdate.return_value = "hi"



    selectionSort = SelectionSort(mock_viewManager, mock_gameWindow)
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

    #WORK---------------------------------------
    selectionSort.Sort(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)


    #ASSERT--------------------------------------
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

  #SwapIndexes---------------------------------------
  def test_SwapWallHeightsIndexes_When_Called(self):
    #SETUP----------------------------------
    #mocking arg objects
    mock_viewManager = Mock()
    mock_gameWindow = Mock()




    selectionSort = SelectionSort(mock_viewManager, mock_gameWindow)
    N = go.NOTHING
    W = go.WALL
    currentGrid = [
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, W, N, N, N],
                  [N, N, N, N, W, N, N, N],
                  [N, W, N, N, W, N, N, N],
                  [N, W, N, N, W, N, W, N],
                  [W, W, N, N, W, N, W, N],
                  [W, W, W, W, W, W, W, W],
                  [W, W, W, W, W, W, W, W],
                                          ]
    currentPastGrids = []
    currentPastGridsIndex = 0
    wallHeights = [3, 5, 2, 2, 7, 2, 4, 2]

    #WORK------------------------------------------
    selectionSort.SwapIndexes(currentGrid, wallHeights, 0, 2, currentPastGrids, currentPastGridsIndex)

    #ASSERT----------------------------------------
    assert wallHeights == [2, 5, 3, 2, 7, 2, 4, 2]

  def test_SwapUIWallHeightsIndexes_When_Called(self):
    #SETUP----------------------------------
    #mocking arg objects
    mock_viewManager = Mock()
    mock_gameWindow = Mock()




    selectionSort = SelectionSort(mock_viewManager, mock_gameWindow)
    N = go.NOTHING
    W = go.WALL
    currentGrid = [
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, W, N, N, N],
                  [N, N, N, N, W, N, N, N],
                  [N, W, N, N, W, N, N, N],
                  [N, W, N, N, W, N, W, N],
                  [W, W, N, N, W, N, W, N],
                  [W, W, W, W, W, W, W, W],
                  [W, W, W, W, W, W, W, W],
                                          ]
    currentPastGrids = []
    currentPastGridsIndex = 0
    wallHeights = [3, 5, 2, 2, 7, 2, 4, 2]

    #WORK------------------------------------------
    selectionSort.SwapIndexes(currentGrid, wallHeights, 0, 2, currentPastGrids, currentPastGridsIndex)

    #ASSERT----------------------------------------
    assert currentGrid == [
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, W, N, N, N],
                          [N, N, N, N, W, N, N, N],
                          [N, W, N, N, W, N, N, N],
                          [N, W, N, N, W, N, W, N],
                          [N, W, W, N, W, N, W, N],
                          [W, W, W, W, W, W, W, W],
                          [W, W, W, W, W, W, W, W],
                                                  ]

if __name__ == "__main__":
  unittest.main()