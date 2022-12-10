import pytest
from unittest.mock import MagicMock, patch
from View.UISolveSortButton import UISolveSortButton


#Draw------------------------------------------------

@pytest.mark.skip(reason="pygame")
def test_ButtonIsCreated_When_Called():
  print("wip")


#ClickButton

@pytest.mark.xfail
def FunctionIsCalled_When_ClickButtonCalled():
  #setup
  uiSolveSortButton = UISolveSortButton()
  returnValue = "none"

  #work
  returnValue = uiSolveSortButton.ClickButton()

  #assert
  assert returnValue == "pointer to Solve method in SolveMazeController or Sort method in SortWallsController"