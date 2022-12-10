import pytest
from unittest.mock import MagicMock, patch
from View.SelectPastGridsDropdown import SelectPastGridsDropdown


#Draw------------------------------------------------

@pytest.mark.skip(reason="pygame")
def test_ButtonIsCreated_When_Called():
  print("wip")


#ClickDropdown---------*INCOMPLETE*-------(think about what this is)

@pytest.mark.xfail
def FunctionIsCalled_When_ClickDropdownCalled():
  #setup
  selectPastGridsDropdown = SelectPastGridsDropdown()
  returnValue = "none"

  #work
  returnValue = selectPastGridsDropdown.ClickDropdown()

  #assert
  assert returnValue == "pointer to (FINISH THIS)"