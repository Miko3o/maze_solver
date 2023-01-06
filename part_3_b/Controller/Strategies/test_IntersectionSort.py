import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from Controller.Strategies.IntersectionSort import IntersectionSort
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



    intersectionSort = IntersectionSort(mock_viewManager, mock_gameWindow)
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
    intersectionSort.Sort(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)


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

  @patch("pygame.display.update")
  @patch("pygame.event.get")
  def test_PygameDisplayFunctionIsCalled_When_SortCalled(self, mock_pygameEventGet, mock_pygameDisplayUpdate):
    #SETUP----------------------------------
    #mocking arg objects
    mock_viewManager = Mock()
    mock_gameWindow = Mock()

    #mock function return value
    mock_pygameEventGet.return_value = []
    mock_pygameDisplayUpdate.return_value = "hi"



    intersectionSort = IntersectionSort(mock_viewManager, mock_gameWindow)
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
    intersectionSort.Sort(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)
    
    #ASSERT-----------------------------------------
    mock_pygameDisplayUpdate.assert_called()
  
  
  #SwapIndexes---------------------------------------
  def test_SwapWallHeightsIndexes_When_Called(self):
    #SETUP----------------------------------
    #mocking arg objects
    mock_viewManager = Mock()
    mock_gameWindow = Mock()




    intersectionSort = IntersectionSort(mock_viewManager, mock_gameWindow)
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
    wallHeights = [1, 5, 2, 2, 7, 2, 4, 2]

    #WORK------------------------------------------
    intersectionSort.SwapIndexes(currentGrid, wallHeights, 2, currentPastGrids, currentPastGridsIndex)

    #ASSERT----------------------------------------
    assert wallHeights == [1, 2, 5, 2, 7, 2, 4, 2]

  def test_SwapUIWallHeightsIndexes_When_Called(self):
    #SETUP----------------------------------
    #mocking arg objects
    mock_viewManager = Mock()
    mock_gameWindow = Mock()




    intersectionSort = IntersectionSort(mock_viewManager, mock_gameWindow)
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
    wallHeights = [1, 5, 2, 2, 7, 2, 4, 2]

    #WORK------------------------------------------
    intersectionSort.SwapIndexes(currentGrid, wallHeights, 2, currentPastGrids, currentPastGridsIndex)

    #ASSERT----------------------------------------
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