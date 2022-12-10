import pytest
from unittest.mock import MagicMock, patch
from Controller.SortWallsController import SortWallsController


#SetData-----------*INCOMPLETE*-------------------

#note: what is this?????

@pytest.mark.xfail
def test_DataIsSet_When_SetDataCalled():
  print("wip")


#Sort--------------------------------------------



@pytest.mark.xfail
def WallsAreSorted_When_SortCalled():
  #setup
  sortWallsController = SortWallsController()
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
  currentGrid = sortWallsController.Sort()


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

#ChangeStrategy--------------------------------------

@pytest.mark.xfail
def StrategyIsChanged_When_ChangeStrategiesCalled():
  #setup
  sortWallsController = SortWallsController()
  currentStrategy = "Bubble Sort"

  #work
  currentStrategy = sortWallsController.ChangeStrategy

  #assert
  assert currentStrategy == "Radix Sort"


#GetAllStrategies-------*INCOMPLETE*--------(dropdown)

@pytest.mark.xfail
def StrategiesAreDisplayed_When_GetAllStrategiesCalled():

  #note: also forgot what this does
  
  #setup
  sortWallsController = SortWallsController()
  print("wip")