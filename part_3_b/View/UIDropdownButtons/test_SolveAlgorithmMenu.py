import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from View.UIDropdownButtons.SolveAlgorithmMenu import SolveAlgorithmMenu


#Draw------------------------------------------------
@patch("pygame.mouse.get_pressed")
@patch("pygame.Surface")
@patch("pygame.font.SysFont")
@patch("pygame.draw.lines")
@patch("pygame.draw.rect")
class Test_SolveAlgorithmMenu(unittest.TestCase):
    def test_MenuIsDrawnWithProperties_When_DrawCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed):
        #SETUP------------------------------------------------------
        #mock class args
        mock_viewManager = Mock()

        #button properties args
        menuColor = (255, 255, 255)
        menuText = ["BFS", "DFS", "Dijkstra", "A*"]
        menuReturn = ["sa.BFS", "sa.DFS", "sa.Dijkstra", "sa.Astar"]
        menuWidth = 70
        menuHeight = 30
        displayX = 52
        displayY = 121
        previousTextHeight = 0
        previousTextSpacing = 0

        #draw function args
        mouseX = 53
        mouseY = 120

        #button class
        solveAlgorithmMenu = SolveAlgorithmMenu(mock_pygameSurface, mock_viewManager, menuText, menuReturn, menuWidth, menuHeight, displayX, displayY)

        #WORK-------------------------------------
        solveAlgorithmMenu.Draw(mouseX, mouseY)

        #ASSERT------------------------------------
        mock_pygameDrawRect.assert_called_with(mock_pygameSurface, menuColor, [displayX, 183, menuWidth, 17])

    #Unclick-----------------------------------------------
    def test_MenuIsUnclickedWithProperties_When_DrawCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed):
        #SETUP------------------------------------------------------
        #mock class args
        mock_viewManager = Mock()

        #button properties args
        menuColor = (255, 255, 255)
        menuText = ["BFS", "DFS", "Dijkstra", "A*"]
        menuReturn = ["sa.BFS", "sa.DFS", "sa.Dijkstra", "sa.Astar"]
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
        solveAlgorithmMenu = SolveAlgorithmMenu(mock_pygameSurface, mock_viewManager, menuText, menuReturn, menuWidth, menuHeight, displayX, displayY)
        solveAlgorithmMenu.clicked = True

        #WORK-------------------------------------
        solveAlgorithmMenu.UnclickOption(mouseX, mouseY)

        #ASSERT------------------------------------
        assert solveAlgorithmMenu.clicked == False



if __name__ == "__main__":
  unittest.main()