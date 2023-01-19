import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from View.UIDropdownButtons.SortAlgorithmDropdown import SortAlgorithmDropdown


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
    buttonText = "Pick Algorithm"
    buttonWidth = 120
    buttonHeight = 30
    displayX = 30
    displayY = 120

    #draw function args
    mouseX = 31
    mouseY = 121
    color = tuple(buttonColor)

    #button class
    sortAlgorithmDropdown = SortAlgorithmDropdown(mock_pygameSurface, buttonColor, buttonText, buttonWidth, buttonHeight, displayX, displayY, mock_viewManager)
    sortAlgorithmDropdown.rect = mock_pygameDrawRect(mock_pygameSurface, (color), [displayX, displayY, buttonWidth, buttonHeight])

    #WORK-------------------------------------
    sortAlgorithmDropdown.Draw(mouseX, mouseY)

    #ASSERT------------------------------------
    mock_pygameDrawRect.assert_called_with(mock_pygameSurface, (color), [displayX, displayY, buttonWidth, buttonHeight])


#ClickButton--------------------------------------
  def test_ButtonIsClickedWithProperties_When_ClickButtonCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed):
    #SETUP------------------------------------------------------
    #mock class args
    mock_viewManager = Mock()

    #button properties args
    buttonColor = [230, 230, 230]
    buttonText = "Pick Algorithm"
    buttonWidth = 120
    buttonHeight = 30
    displayX = 30
    displayY = 120

    #draw function args
    mouseX = 31
    mouseY = 121
    color = tuple(buttonColor)
    mock_pygameMouseGetPressed.return_value = [1]

    #button class
    sortAlgorithmDropdown = SortAlgorithmDropdown(mock_pygameSurface, buttonColor, buttonText, buttonWidth, buttonHeight, displayX, displayY, mock_viewManager)
    sortAlgorithmDropdown.rect = mock_pygameDrawRect(mock_pygameSurface, (color), [displayX, displayY, buttonWidth, buttonHeight])

    #button method
    sortAlgorithmDropdown.rect.collidepoint.return_value = True

    #WORK-------------------------------------
    sortAlgorithmDropdown.ClickButton(mouseX, mouseY)

    #ASSERT------------------------------------
    assert sortAlgorithmDropdown.clicked == True



if __name__ == "__main__":
  unittest.main()