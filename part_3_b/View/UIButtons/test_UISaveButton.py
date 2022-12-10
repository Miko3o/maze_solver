import pytest
from unittest.mock import MagicMock, patch
from View.UISaveButton import UISaveButton


#Draw------------------------------------------------

@pytest.mark.skip(reason="pygame")
def test_ButtonIsCreated_When_Called():
  print("wip")


#ClickButton

@pytest.mark.xfail
def FunctionIsCalled_When_ClickButtonCalled():
  #setup
  uiSaveButton = UISaveButton()
  returnValue = "none"

  #work
  returnValue = uiSaveButton.ClickButton()

  #assert
  assert returnValue == "pointer to Save method in SaveMazeController"