import pytest
from unittest.mock import MagicMock, patch
from View.UILoadButton import UILoadButton


#Draw------------------------------------------------

@pytest.mark.skip(reason="pygame")
def test_ButtonIsCreated_When_Called():
  print("wip")


#ClickButton

@pytest.mark.xfail
def FunctionIsCalled_When_ClickButtonCalled():
  #setup
  uiLoadButton = UILoadButton()
  returnValue = "none"

  #work
  returnValue = uiLoadButton.ClickButton()

  #assert
  assert returnValue == "pointer to Load method in LoadMazeController"