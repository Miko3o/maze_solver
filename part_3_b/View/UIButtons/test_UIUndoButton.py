import pytest
from unittest.mock import MagicMock, patch
from View.UIUndoButton import UIUndoButton


#Draw------------------------------------------------

@pytest.mark.skip(reason="pygame")
def test_ButtonIsCreated_When_Called():
  print("wip")


#ClickButton

@pytest.mark.xfail
def FunctionIsCalled_When_ClickButtonCalled():
  #setup
  uiUndoButton = UIUndoButton()
  returnValue = "none"

  #work
  returnValue = uiUndoButton.ClickButton()

  #assert
  assert returnValue == "pointer to Undo method in UndoController"