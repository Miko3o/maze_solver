import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from View.UIButtons.UISaveButton import UISaveButton


#Draw------------------------------------------------
@patch("pygame.mouse.get_pressed")
@patch("pygame.Surface")
@patch("pygame.font.SysFont")
@patch("pygame.draw.lines")
@patch("pygame.draw.rect")
class Test_UISaveButton(unittest.TestCase):
  def test_ButtonIsDrawnWithProperties_When_DrawCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed):
    #SETUP------------------------------------------------------
    #mock class args
    mock_viewManager = Mock()

    #button properties args
    buttonColor = [255, 150, 173]
    buttonOutlineColor = (139, 49, 73)
    buttonText = "Save"
    buttonWidth = 75
    buttonHeight = 30
    displayX = 130
    displayY = 17

    #draw function args
    mouseX = 131
    mouseY = 18
    color = tuple(buttonColor)

    #button class
    uISaveButton = UISaveButton(mock_pygameSurface, mock_viewManager, buttonColor, buttonOutlineColor, buttonText, buttonWidth, buttonHeight, displayX, displayY)
    uISaveButton.rect = mock_pygameDrawRect(mock_pygameSurface, (color), [displayX, displayY, buttonWidth, buttonHeight])

    #WORK-------------------------------------
    uISaveButton.Draw(mouseX, mouseY)

    #ASSERT------------------------------------
    mock_pygameDrawRect.assert_called_with(mock_pygameSurface, (color), [displayX, displayY, buttonWidth, buttonHeight])


#ClickButton--------------------------------------
  def test_ButtonIsClickedWithProperties_When_ClickButtonCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed):
    #SETUP------------------------------------------------------
    #mock class args
    mock_viewManager = Mock()

    #button properties args
    buttonColor = [255, 150, 173]
    buttonOutlineColor = (139, 49, 73)
    buttonText = "Save"
    buttonWidth = 75
    buttonHeight = 30
    displayX = 130
    displayY = 17

    #draw function args
    mouseX = 131
    mouseY = 18
    color = tuple(buttonColor)
    mock_pygameMouseGetPressed.return_value = [1]

    #button class
    uISaveButton = UISaveButton(mock_pygameSurface, mock_viewManager, buttonColor, buttonOutlineColor, buttonText, buttonWidth, buttonHeight, displayX, displayY)
    uISaveButton.rect = mock_pygameDrawRect(mock_pygameSurface, (color), [displayX, displayY, buttonWidth, buttonHeight])

    #button method
    uISaveButton.rect.collidepoint.return_value = True

    #WORK-------------------------------------
    uISaveButton.ClickButton(mouseX, mouseY)

    #ASSERT------------------------------------
    assert uISaveButton.clicked == True

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
    mock_pygameMouseGetPressed.return_value = [0]

    #button class
    uISaveButton = UISaveButton(mock_pygameSurface, mock_viewManager, buttonColor, buttonOutlineColor, buttonText, buttonWidth, buttonHeight, displayX, displayY)
    uISaveButton.rect = mock_pygameDrawRect(mock_pygameSurface, (color), [displayX, displayY, buttonWidth, buttonHeight])
    uISaveButton.clicked = True

    #WORK-------------------------------------
    uISaveButton.UnclickButton(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)

    #ASSERT------------------------------------
    assert uISaveButton.clicked == False


if __name__ == "__main__":
  unittest.main()