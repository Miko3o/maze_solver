import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from Controller.Strategies.MergeSort import MergeSort
from View.GameStateENUM import GridObjects as go

#Sort--------------------------------------------


class Test_MergeSort(unittest.TestCase):
  @patch("pygame.display.update")
  @patch("pygame.event.get")
  def test_UIWallsAreSorted_When_SortCalled(self, mock_pygameEventGet, mock_pygameDisplayUpdate):
    #SETUP-----------------------------------
    #mocking arg objects
    mock_viewManager = Mock()
    mock_gameWindow = Mock()

    #mock function return value
    mock_pygameEventGet.return_value = []
    mock_pygameDisplayUpdate.return_value = "hi"


    mergeSort = MergeSort(mock_viewManager, mock_gameWindow)
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

    #WORK--------------------------------------
    mergeSort.Sort(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)


    #ASSERT-------------------------------------
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

  #MergeSort--------------------------------------
  @patch("pygame.display.update")
  @patch("pygame.event.get")
  def test_ArraysAreMergedAndSorted_When_MergeSortCalled(self, mock_pygameEventGet, mock_pygameDisplayUpdate):
    #SETUP-----------------------------------
    #mocking arg objects
    mock_viewManager = Mock()
    mock_gameWindow = Mock()

    #mock function return value
    mock_pygameEventGet.return_value = []
    mock_pygameDisplayUpdate.return_value = "hi"


    mergeSort = MergeSort(mock_viewManager, mock_gameWindow)
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
    wallHeights = [1, 5]


    #WORK-------------------------------------
    mergeSort.MergeSort(wallHeights, currentGrid)


    #ASSERT-----------------------------------
    assert wallHeights == [1,5]