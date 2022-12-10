import pytest
from unittest.mock import MagicMock, patch
from View.SelectGridObjectDropdown import SelectGridObjectDropdown


#Draw------------------------------------------------

@pytest.mark.skip(reason="pygame")
def test_ButtonIsCreated_When_Called():
  print("wip")


#ClickDropdown---------*INCOMPLETE*-------------

@pytest.mark.xfail
def FunctionIsCalled_When_ClickDropdownCalled():
  #setup
  selectGridObjectDropdown = SelectGridObjectDropdown()
  returnValue = "none"

  #work
  returnValue = selectGridObjectDropdown.ClickDropdown()

  #assert
  assert returnValue == "pointer to GetAllGridObjects in GridObjectController"