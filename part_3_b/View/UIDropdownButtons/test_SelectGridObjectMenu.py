import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from View.UIDropdownButtons.SelectGridObjectMenu import SelectGridObjectMenu


#Draw------------------------------------------------
@patch("pygame.mouse.get_pressed")
@patch("pygame.Surface")
@patch("pygame.font.SysFont")
@patch("pygame.draw.lines")
@patch("pygame.draw.rect")
class Test_SelectGridObjectMenu(unittest.TestCase):
    def test_MenuIsDrawnWithProperties_When_DrawCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed):
        #SETUP------------------------------------------------------
        #mock class args
        mock_viewManager = Mock()

        #button properties args
        menuColor = (255, 255, 255)
        menuText = ["Wall", "Solver", "Goal"]
        menuReturn = ["go.WALL", "go.SOLVER", "go.GOAL"]
        menuWidth = 70
        menuHeight = 30
        displayX = 52
        displayY = 120
        previousTextHeight = 0
        previousTextSpacing = 0

        #draw function args
        mouseX = 53
        mouseY = 121

        #button class
        selectGridObjectMenu = SelectGridObjectMenu(mock_pygameSurface, mock_viewManager, menuText, menuReturn, menuWidth, menuHeight, displayX, displayY)

        #WORK-------------------------------------
        selectGridObjectMenu.Draw(mouseX, mouseY)

        #ASSERT------------------------------------
        mock_pygameDrawRect.assert_called_with(mock_pygameSurface, menuColor, [displayX, 163, menuWidth, 17])

    #Unclick-----------------------------------------------
    def test_MenuIsUnclickedWithProperties_When_DrawCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed):
        #SETUP------------------------------------------------------
        #mock class args
        mock_viewManager = Mock()

        #button properties args
        menuColor = (255, 255, 255)
        menuText = ["Wall", "Solver", "Goal"]
        menuReturn = ["go.WALL", "go.SOLVER", "go.GOAL"]
        menuWidth = 70
        menuHeight = 30
        displayX = 52
        displayY = 120
        previousTextHeight = 0
        previousTextSpacing = 0

        #draw function args
        mouseX = 53
        mouseY = 121
        mock_pygameMouseGetPressed.return_value = [0]

        #button class
        selectGridObjectMenu = SelectGridObjectMenu(mock_pygameSurface, mock_viewManager, menuText, menuReturn, menuWidth, menuHeight, displayX, displayY)
        selectGridObjectMenu.clicked = True

        #WORK-------------------------------------
        selectGridObjectMenu.UnclickOption(mouseX, mouseY)

        #ASSERT------------------------------------
        assert selectGridObjectMenu.clicked == False



if __name__ == "__main__":
  unittest.main()