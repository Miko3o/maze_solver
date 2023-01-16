from View.GameStateENUM import SortingAlgorithm as sra


class SortWallsController():

  def __init__(self, controllerManager, viewManager):
    self.controllerManager = controllerManager
    self.viewManager = viewManager
    self.sortingAlgorithm = sra.BubbleSort


  def Sort(self, currentGrid, gridSize, currentPastGrids, currentPastGridsIndex):
    if self.sortingAlgorithm == sra.BubbleSort:
      self.controllerManager.bubbleSort.Sort(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)
    elif self.sortingAlgorithm == sra.IntersectionSort:
      self.controllerManager.intersectionSort.Sort(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)
    elif self.sortingAlgorithm == sra.MergeSort:
      self.controllerManager.mergeSort.Sort(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)
    elif self.sortingAlgorithm == sra.QuickSort:
      self.controllerManager.quickSort.Sort(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)
    elif self.sortingAlgorithm == sra.RadixSort:
      self.controllerManager.radixSort.Sort(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)
    elif self.sortingAlgorithm == sra.SelectionSort:
      self.controllerManager.selectionSort.Sort(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)

  def ChangeStrategy(self, newStrategy):
    self.sortingAlgorithm = newStrategy
    print("newStrategy:", self.sortingAlgorithm)