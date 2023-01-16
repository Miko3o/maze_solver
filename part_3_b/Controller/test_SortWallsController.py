import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from Controller.SortWallsController import SortWallsController
from View.GameStateENUM import GridObjects as go, SortingAlgorithm as sra


class Test_SortWallsController(unittest.TestCase):
  def test_WallsSortedUsingBubbleSort_When_SortWallsControllerCalled(self):
    #SETUP-------------------------------------------------
    #mock args
    mock_controllerManager = Mock()
    mock_viewManager = Mock()

    sortWallsController = SortWallsController(mock_controllerManager, mock_viewManager)
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
    sortWallsController.sortingAlgorithm = sra.BubbleSort
    gridSize = 8
    currentPastGrids = []
    currentPastGridsIndex = 0

    #WORK-----------------------------------
    sortWallsController.Sort(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)


    #ASSERT--------------------------------
    sortWallsController.controllerManager.bubbleSort.Sort.assert_called

  def test_WallsSortedUsingIntersectionSort_When_SortWallsControllerCalled(self):
    #SETUP-------------------------------------------------
    #mock args
    mock_controllerManager = Mock()
    mock_viewManager = Mock()

    sortWallsController = SortWallsController(mock_controllerManager, mock_viewManager)
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
    sortWallsController.sortingAlgorithm = sra.IntersectionSort
    gridSize = 8
    currentPastGrids = []
    currentPastGridsIndex = 0

    #WORK-----------------------------------
    sortWallsController.Sort(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)


    #ASSERT--------------------------------
    sortWallsController.controllerManager.intersectionSort.Sort.assert_called

  def test_WallsSortedUsingMergeSort_When_SortWallsControllerCalled(self):
    #SETUP-------------------------------------------------
    #mock args
    mock_controllerManager = Mock()
    mock_viewManager = Mock()

    sortWallsController = SortWallsController(mock_controllerManager, mock_viewManager)
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
    sortWallsController.sortingAlgorithm = sra.MergeSort
    gridSize = 8
    currentPastGrids = []
    currentPastGridsIndex = 0

    #WORK-----------------------------------
    sortWallsController.Sort(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)


    #ASSERT--------------------------------
    sortWallsController.controllerManager.mergeSort.Sort.assert_called

  def test_WallsSortedUsingQuickSortSort_When_SortWallsControllerCalled(self):
    #SETUP-------------------------------------------------
    #mock args
    mock_controllerManager = Mock()
    mock_viewManager = Mock()

    sortWallsController = SortWallsController(mock_controllerManager, mock_viewManager)
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
    sortWallsController.sortingAlgorithm = sra.QuickSort
    gridSize = 8
    currentPastGrids = []
    currentPastGridsIndex = 0

    #WORK-----------------------------------
    sortWallsController.Sort(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)


    #ASSERT--------------------------------
    sortWallsController.controllerManager.quickSort.Sort.assert_called

  def test_WallsSortedUsingRadixSort_When_SortWallsControllerCalled(self):
    #SETUP-------------------------------------------------
    #mock args
    mock_controllerManager = Mock()
    mock_viewManager = Mock()

    sortWallsController = SortWallsController(mock_controllerManager, mock_viewManager)
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
    sortWallsController.sortingAlgorithm = sra.RadixSort
    gridSize = 8
    currentPastGrids = []
    currentPastGridsIndex = 0

    #WORK-----------------------------------
    sortWallsController.Sort(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)


    #ASSERT--------------------------------
    sortWallsController.controllerManager.radixSort.Sort.assert_called

  def test_WallsSortedUsingSelectionSort_When_SortWallsControllerCalled(self):
    #SETUP-------------------------------------------------
    #mock args
    mock_controllerManager = Mock()
    mock_viewManager = Mock()

    sortWallsController = SortWallsController(mock_controllerManager, mock_viewManager)
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
    sortWallsController.sortingAlgorithm = sra.SelectionSort
    gridSize = 8
    currentPastGrids = []
    currentPastGridsIndex = 0

    #WORK-----------------------------------
    sortWallsController.Sort(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)


    #ASSERT--------------------------------
    sortWallsController.controllerManager.selecetionSort.Sort.assert_called



  #ChangeStrategy--------------------------------------
  def test_StrategyIsChangedToIntersection_When_ChangeStrategiesCalled(self):
    #SETUP-------------------------------------------------
    #mock args
    mock_controllerManager = Mock()
    mock_viewManager = Mock()

    sortWallsController = SortWallsController(mock_controllerManager, mock_viewManager)
    sortWallsController.sortingAlgorithm = sra.BubbleSort
    newStrategy = sra.IntersectionSort

    #WORK----------------------------------
    sortWallsController.ChangeStrategy(newStrategy)

    #ASSERT----------------------------------
    assert sortWallsController.sortingAlgorithm == sra.IntersectionSort

if __name__ == "__main__":
  unittest.main()