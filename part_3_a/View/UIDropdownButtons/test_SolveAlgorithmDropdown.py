import pytest
from unittest.mock import MagicMock, patch
from View.SolveAlgorithmDropdown import SolveAlgorithmDropdown


#Draw------------------------------------------------

@pytest.mark.skip(reason="pygame")
def test_ButtonIsCreated_When_Called():
  print("wip")


#ClickDropdown---------*INCOMPLETE*-------------

@pytest.mark.xfail
def FunctionIsCalled_When_ClickDropdownCalled():
  #setup
  solveAlgorithmDropdown = SolveAlgorithmDropdown()
  returnValue = "none"

  #work
  returnValue = solveAlgorithmDropdown.ClickDropdown()

  #assert
  assert returnValue == "pointer to GetAllStrategies in SolveMazeController"