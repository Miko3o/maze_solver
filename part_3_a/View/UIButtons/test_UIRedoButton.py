import pytest
from unittest.mock import MagicMock, patch
from View.UIRedoButton import UIRedoButton


#Draw------------------------------------------------

@pytest.mark.skip(reason="pygame")
def test_ButtonIsCreated_When_Called():
  print("wip")


#ClickButton

@pytest.mark.xfail
def FunctionIsCalled_When_ClickButtonCalled():
  #setup
  uiRedoButton = UIRedoButton()
  returnValue = "none"

  #work
  returnValue = uiRedoButton.ClickButton()

  #assert
  assert returnValue == "pointer to Redo method in RedoController"