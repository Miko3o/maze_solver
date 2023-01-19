import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from View.UIDropdownButtons.SelectGridObjectDropdown import SelectGridObjectDropdown


#Draw------------------------------------------------
@patch("pygame.mouse.get_pressed")
@patch("pygame.Surface")
@patch("pygame.font.SysFont")
@patch("pygame.draw.lines")
@patch("pygame.draw.rect")
class Test_SelectGridObjectDropdown(unittest.TestCase):
  def test_ButtonIsDrawnWithProperties_When_DrawCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed):
    #SETUP------------------------------------------------------
    #mock class args
    mock_viewManager = Mock()

    #button properties args
    buttonColor = [230, 230, 230]
    buttonText = "Select Object"
    buttonWidth = 120
    buttonHeight = 30
    displayX = 30
    displayY = 80

    #draw function args
    mouseX = 31
    mouseY = 81
    color = tuple(buttonColor)

    #button class
    selectGridObjectDropdown = SelectGridObjectDropdown(mock_pygameSurface, buttonColor, buttonText, buttonWidth, buttonHeight, displayX, displayY, mock_viewManager)
    selectGridObjectDropdown.rect = mock_pygameDrawRect(mock_pygameSurface, (color), [displayX, displayY, buttonWidth, buttonHeight])

    #WORK-------------------------------------
    selectGridObjectDropdown.Draw(mouseX, mouseY)

    #ASSERT------------------------------------
    mock_pygameDrawRect.assert_called_with(mock_pygameSurface, (color), [displayX, displayY, buttonWidth, buttonHeight])


#ClickButton--------------------------------------
  def test_ButtonIsClickedWithProperties_When_ClickButtonCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed):
    #SETUP------------------------------------------------------
    #mock class args
    mock_viewManager = Mock()

    #button properties args
    buttonColor = [230, 230, 230]
    buttonText = "Select Object"
    buttonWidth = 120
    buttonHeight = 30
    displayX = 30
    displayY = 80

    #draw function args
    mouseX = 31
    mouseY = 81
    color = tuple(buttonColor)
    mock_pygameMouseGetPressed.return_value = [1]

    #button class
    selectGridObjectDropdown = SelectGridObjectDropdown(mock_pygameSurface, buttonColor, buttonText, buttonWidth, buttonHeight, displayX, displayY, mock_viewManager)
    selectGridObjectDropdown.rect = mock_pygameDrawRect(mock_pygameSurface, (color), [displayX, displayY, buttonWidth, buttonHeight])

    #button method
    selectGridObjectDropdown.rect.collidepoint.return_value = True

    #WORK-------------------------------------
    selectGridObjectDropdown.ClickButton(mouseX, mouseY)

    #ASSERT------------------------------------
    assert selectGridObjectDropdown.clicked == True

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
    selectGridObjectDropdown = SelectGridObjectDropdown(mock_pygameSurface, buttonColor, buttonText, buttonWidth, buttonHeight, displayX, displayY, mock_viewManager)
    selectGridObjectDropdown.rect = mock_pygameDrawRect(mock_pygameSurface, (color), [displayX, displayY, buttonWidth, buttonHeight])
    selectGridObjectDropdown.clicked = True

    #WORK-------------------------------------
    selectGridObjectDropdown.UnclickButton(currentGrid, gridSize, currentPastGrids, currentPastGridsIndex)

    #ASSERT------------------------------------
    assert selectGridObjectDropdown.clicked == False


if __name__ == "__main__":
  unittest.main()