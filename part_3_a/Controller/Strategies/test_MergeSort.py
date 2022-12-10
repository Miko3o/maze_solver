import pytest
from unittest.mock import MagicMock, patch
from Controller.Strategies.MergeSort import MergeSort

#Sort--------------------------------------------



@pytest.mark.xfail
def WallsAreSorted_When_SortCalled():
  #setup
  mergeSort = MergeSort()
  N = "nothing"
  W = "wall"
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

  #work
  currentGrid = mergeSort.Sort()


  #assert
  assert   currentGrid == [
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, W],
                          [N, N, N, N, N, N, N, W],
                          [N, N, N, N, N, N, W, W],
                          [N, N, N, N, N, W, W, W],
                          [N, N, N, N, N, W, W, W],
                          [N, W, W, W, W, W, W, W],
                          [W, W, W, W, W, W, W, W],
                                                  ]