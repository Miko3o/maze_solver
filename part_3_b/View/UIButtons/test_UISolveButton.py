import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from View.UIButtons.UISolveButton import UISolveButton


#Draw------------------------------------------------
@patch("pygame.mouse.get_pressed")
@patch("pygame.Surface")
@patch("pygame.font.SysFont")
@patch("pygame.draw.lines")
@patch("pygame.draw.rect")
class Test_UISolveButton(unittest.TestCase):
  def test_ButtonIsDrawnWithProperties_When_DrawCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed):
    #SETUP------------------------------------------------------
    #mock class args
    mock_viewManager = Mock()

    #button properties args
    buttonColor = [255, 205, 119]
    buttonOutlineColor = (169, 119, 33)
    buttonText = "SOLVE"
    buttonWidth = 100
    buttonHeight = 70
    displayX = 472
    displayY = 70

    #draw function args
    mouseX = 473
    mouseY = 71
    color = tuple(buttonColor)

    #button class
    uiSolveButton = UISolveButton(mock_pygameSurface, mock_viewManager, buttonColor, buttonOutlineColor, buttonText, buttonWidth, buttonHeight, displayX, displayY)
    uiSolveButton.rect = mock_pygameDrawRect(mock_pygameSurface, (color), [displayX, displayY, buttonWidth, buttonHeight])

    #WORK-------------------------------------
    uiSolveButton.Draw(mouseX, mouseY)

    #ASSERT------------------------------------
    mock_pygameDrawRect.assert_called_with(mock_pygameSurface, (color), [displayX, displayY, buttonWidth, buttonHeight])


#ClickButton--------------------------------------
  def test_ButtonIsClickedWithProperties_When_ClickButtonCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed):
    #SETUP------------------------------------------------------
    #mock class args
    mock_viewManager = Mock()

    #button properties args
    buttonColor = [255, 205, 119]
    buttonOutlineColor = (169, 119, 33)
    buttonText = "SOLVE"
    buttonWidth = 100
    buttonHeight = 70
    displayX = 472
    displayY = 70

    #draw function args
    mouseX = 473
    mouseY = 71
    color = tuple(buttonColor)
    mock_pygameMouseGetPressed[0].return_value = 1

    #button class
    uiSolveButton = UISolveButton(mock_pygameSurface, mock_viewManager, buttonColor, buttonOutlineColor, buttonText, buttonWidth, buttonHeight, displayX, displayY)
    uiSolveButton.rect = mock_pygameDrawRect(mock_pygameSurface, (color), [displayX, displayY, buttonWidth, buttonHeight])

    #button method
    uiSolveButton.rect.collidepoint.return_value = True

    #WORK-------------------------------------
    uiSolveButton.ClickButton(mouseX, mouseY)

    #ASSERT------------------------------------
    assert uiSolveButton.clicked == True

  #unclick button-----------------------------------------
  def test_ButtonIsUnclickedWithProperties_When_UnclickButtonCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed):
    #SETUP------------------------------------------------------
    #mock class args
    mock_viewManager = Mock()

    #button properties args
    buttonColor = [0, 0, 0]
    buttonOutlineColor = (0, 0, 0)
    buttonText = "mock"
    buttonWidth = 0
    buttonHeight = 0
    displayX = 0
    displayY = 0

    #grid args
    currentGrid =[]
    gridSize = 0
    currentPastGrids = []
    currentPastGridsIndex = 0
    gameState = 0

    #draw function args
    color = tuple(buttonColor)
    mock_pygameMouseGetPressed[0].return_value = 0

    #button class
    uiSolveButton = UISolveButton(mock_pygameSurface, mock_viewManager, buttonColor, buttonOutlineColor, buttonText, buttonWidth, buttonHeight, displayX, displayY)
    uiSolveButton.rect = mock_pygameDrawRect(mock_pygameSurface, (color), [displayX, displayY, buttonWidth, buttonHeight])
    uiSolveButton.clicked = True

    #WORK-------------------------------------
    uiSolveButton.UnclickButton(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)

    #ASSERT------------------------------------
    assert uiSolveButton.clicked == False


if __name__ == "__main__":
  unittest.main()