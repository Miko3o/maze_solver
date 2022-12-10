import pytest
from unittest.mock import MagicMock, patch
from View.UIGravityButton import UIGravityButton


#Draw------------------------------------------------

@pytest.mark.skip(reason="pygame")
def test_ButtonIsCreated_When_Called():
  print("wip")


#ClickButton

@pytest.mark.xfail
def FunctionIsCalled_When_ClickButtonCalled():
  #setup
  uiGravityButton = UIGravityButton()
  returnValue = "none"

  #work
  returnValue = uiGravityButton.ClickButton()

  #assert
  assert returnValue == "pointer to Gravity method in GravityController"