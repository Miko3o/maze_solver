import pytest
from unittest.mock import MagicMock, patch
from View.SortAlgorithmDropdown import SortAlgorithmDropdown


#Draw------------------------------------------------

@pytest.mark.skip(reason="pygame")
def test_ButtonIsCreated_When_Called():
  print("wip")


#ClickDropdown---------*INCOMPLETE*-------------

@pytest.mark.xfail
def FunctionIsCalled_When_ClickDropdownCalled():
  #setup
  sortAlgorithmDropdown = SortAlgorithmDropdown()
  returnValue = "none"

  #work
  returnValue = sortAlgorithmDropdown.ClickDropdown()

  #assert
  assert returnValue == "pointer to GetAllStrategies in SortWallsController"