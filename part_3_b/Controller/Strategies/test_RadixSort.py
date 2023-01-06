import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from Controller.Strategies.RadixSort import RadixSort
from View.GameStateENUM import GridObjects as go

#Sort--------------------------------------------


class Test_RadixSort(unittest.TestCase):
  @patch("pygame.display.update")
  @patch("pygame.event.get")
  def test_UIWallsSorted_When_SortCalled(self, mock_pygameEventGet, mock_pygameDisplayUpdate):
    #SETUP----------------------------------
    #mocking arg objects
    mock_viewManager = Mock()
    mock_gameWindow = Mock()

    #mock function return value
    mock_pygameEventGet.return_value = []
    mock_pygameDisplayUpdate.return_value = "hi"


    radixSort = RadixSort(mock_viewManager, mock_gameWindow)
    N = go.NOTHING
    W = go.WALL
    currentGrid = [
                  [N, N, N, N, N, N, N, N, W, N, N, N],
                  [N, N, N, N, N, N, N, N, W, W, N, N],
                  [N, N, N, N, N, N, N, N, W, W, W, N],
                  [N, N, N, N, N, N, N, N, W, W, W, W],
                  [N, N, N, N, N, N, N, N, W, W, W, W],
                  [N, N, N, N, N, N, N, W, W, W, W, W],
                  [N, N, N, N, N, N, N, W, W, W, W, W],
                  [N, N, N, N, N, N, W, W, W, W, W, W],
                  [N, N, N, N, N, W, W, W, W, W, W, W],
                  [N, N, N, N, N, W, W, W, W, W, W, W],
                  [N, W, W, W, W, W, W, W, W, W, W, W],
                  [W, W, W, W, W, W, W, W, W, W, W, W]
                                                      ]
    gridSize = 12
    currentPastGrids = []
    currentPastGridsIndex = 0

    #WORK------------------------------------------
    radixSort.Sort(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)

    #ASSERT----------------------------------------
    assert currentGrid == [
                          [N, N, N, N, N, N, N, N, N, N, N, W],
                          [N, N, N, N, N, N, N, N, N, N, W, W],
                          [N, N, N, N, N, N, N, N, N, W, W, W],
                          [N, N, N, N, N, N, N, N, W, W, W, W],
                          [N, N, N, N, N, N, N, N, W, W, W, W],
                          [N, N, N, N, N, N, N, W, W, W, W, W],
                          [N, N, N, N, N, N, N, W, W, W, W, W],
                          [N, N, N, N, N, N, W, W, W, W, W, W],
                          [N, N, N, N, N, W, W, W, W, W, W, W],
                          [N, N, N, N, N, W, W, W, W, W, W, W],
                          [N, W, W, W, W, W, W, W, W, W, W, W],
                          [W, W, W, W, W, W, W, W, W, W, W, W]
                                                              ]

  #CountingSort-------------------------------------
  @patch("pygame.display.update")
  @patch("pygame.event.get")
  def test_TensPlaceSorted_When_CountingSortCalled(self, mock_pygameEventGet, mock_pygameDisplayUpdate):
    #SETUP----------------------------------
    #mocking arg objects
    mock_viewManager = Mock()
    mock_gameWindow = Mock()

    #mock function return value
    mock_pygameEventGet.return_value = []
    mock_pygameDisplayUpdate.return_value = "hi"


    radixSort = RadixSort(mock_viewManager, mock_gameWindow)
    N = go.NOTHING
    W = go.WALL
    currentGrid = [
                  [N, N, N, N, N, N, N, N, W, N, N, N],
                  [N, N, N, N, N, N, N, N, W, W, N, N],
                  [N, N, N, N, N, N, N, N, W, W, W, N],
                  [N, N, N, N, N, N, N, N, W, W, W, W],
                  [N, N, N, N, N, N, N, N, W, W, W, W],
                  [N, N, N, N, N, N, N, W, W, W, W, W],
                  [N, N, N, N, N, N, N, W, W, W, W, W],
                  [N, N, N, N, N, N, W, W, W, W, W, W],
                  [N, N, N, N, N, W, W, W, W, W, W, W],
                  [N, N, N, N, N, W, W, W, W, W, W, W],
                  [N, W, W, W, W, W, W, W, W, W, W, W],
                  [W, W, W, W, W, W, W, W, W, W, W, W]
                                                      ]
    wallHeights = [1, 2, 2, 2, 2, 4, 5, 7, 12, 11, 10, 9]

    #WORK------------------------------------------
    radixSort.countingSort(wallHeights, 1, currentGrid)

    #ASSERT----------------------------------------
    assert currentGrid == [
                          [N, N, N, N, N, N, N, W, N, N, N, N],
                          [N, N, W, N, N, N, N, W, N, N, N, N],
                          [W, N, W, N, N, N, N, W, N, N, N, N],
                          [W, N, W, N, N, N, N, W, N, N, N, W],
                          [W, N, W, N, N, N, N, W, N, N, N, W],
                          [W, N, W, N, N, N, N, W, N, N, W, W],
                          [W, N, W, N, N, N, N, W, N, N, W, W],
                          [W, N, W, N, N, N, N, W, N, W, W, W],
                          [W, N, W, N, N, N, N, W, W, W, W, W],
                          [W, N, W, N, N, N, N, W, W, W, W, W],
                          [W, N, W, W, W, W, W, W, W, W, W, W],
                          [W, W, W, W, W, W, W, W, W, W, W, W]
                                                              ]
  
  #UpdateUI-----------------------------------
  @patch("pygame.display.update")
  @patch("pygame.event.get")
  def test_SwapUIWallHeightsIndexes_When_Called(self, mock_pygameEventGet, mock_pygameDisplayUpdate):
    #SETUP----------------------------------
    #mocking arg objects
    mock_viewManager = Mock()
    mock_gameWindow = Mock()

    #mock function return value
    mock_pygameEventGet.return_value = []
    mock_pygameDisplayUpdate.return_value = "hi"


    radixSort = RadixSort(mock_viewManager, mock_gameWindow)
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
    UIwallHeights = [1, 2, 5, 2, 7, 2, 4, 2]
 

    #WORK------------------------------------------
    radixSort.UpdateUI(currentGrid, UIwallHeights)

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

  #Gravity-----------------------------------------
  def test_GravityWorks_When_GravityCalled(self):
    #SETUP----------------------------------
    #mocking arg objects
    mock_viewManager = Mock()
    mock_gameWindow = Mock()



    radixSort = RadixSort(mock_viewManager, mock_gameWindow)
    N = go.NOTHING
    W = go.WALL
    currentGrid = [
                  [W, W, W, W, W, W, W, W],
                  [N, W, W, W, W, W, W, W],
                  [N, W, N, N, W, N, W, N],
                  [N, W, N, N, W, N, W, N],
                  [N, W, N, N, W, N, N, N],
                  [N, N, N, N, W, N, N, N],
                  [N, N, N, N, W, N, N, N],
                  [N, N, N, N, N, N, N, N],
                                          ]
 

    #WORK------------------------------------------
    radixSort.Gravity(currentGrid)

    #ASSERT----------------------------------------
    assert currentGrid == [
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, W, N, N, N],
                          [N, N, N, N, W, N, N, N],
                          [N, W, N, N, W, N, N, N],
                          [N, W, N, N, W, N, W, N],
                          [N, W, N, N, W, N, W, N],
                          [N, W, W, W, W, W, W, W],
                          [W, W, W, W, W, W, W, W],
                                                  ]
                                                    
if __name__ == "__main__":
  unittest.main()