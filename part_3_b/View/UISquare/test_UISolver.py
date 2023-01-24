import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from View.UISquare.UISolver import UISolver
from View.GameStateENUM import GridObjects as go


#Draw------------------------------------------------
@patch('pygame.draw.rect')
@patch("pygame.mouse.get_pressed")
@patch("pygame.Surface")
@patch("pygame.font.SysFont")
@patch("pygame.draw.lines")
@patch("pygame.draw.rect")
class Test_UISolver(unittest.TestCase):
    def test_UISquareIsDrawnWithProperties_When_DrawCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed, mock_squareSpace):
        #SETUP------------------------------------------------------
        #mock class args
        mock_viewManager = Mock()
        mock_uiGrid = Mock()

        #grid
        N = go.NOTHING
        W = go.WALL
        S = go.SOLVER
        G = go.GOAL
        P = go.PATH
        F = go.FINDER
        currentGrid = [
                [G, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                                        ]

        #draw function args
        mouseX = 161
        mouseY = 60
        gridRow = 0
        square = 0
        lineStartPositionx = 160
        lineStartPositiony = 60
        distanceBetweenRows = 35
        positions = [lineStartPositionx, lineStartPositiony, distanceBetweenRows, distanceBetweenRows]

        #button class
        uiSolver = UISolver(mock_uiGrid)

        #WORK-------------------------------------
        uiSolver.Draw(mock_pygameSurface, currentGrid, gridRow, square, lineStartPositionx, lineStartPositiony, distanceBetweenRows)

        #ASSERT------------------------------------
        mock_pygameDrawRect.assert_called

    #Click-----------------------------------------------
    def test_UISquareIsLeftClickedWithProperties_When_DrawCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed, mock_squareSpace):
        #SETUP------------------------------------------------------
        #mock class args
        mock_viewManager = Mock()
        mock_uiGrid = Mock()

        #grid
        N = go.NOTHING
        W = go.WALL
        S = go.SOLVER
        G = go.GOAL
        P = go.PATH
        F = go.FINDER
        currentGrid = [
                [G, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                                        ]

        #draw function args
        mouseX = 161
        mouseY = 61
        gridRow = 0
        square = 0
        currentGridIndex = 0
        currentGridObject = go.WALL
        pastGrids = []
        mock_pygameMouseGetPressed.return_value = [1, 0, 0]
        mock_squareSpace.collidepoint.return_value = True

        #button class
        uiSolver = UISolver(mock_uiGrid)

        #WORK-------------------------------------
        uiSolver.ClickGrid(mouseX, mouseY, gridRow, square, mock_squareSpace, currentGridIndex, currentGridObject, currentGrid, pastGrids)

        #ASSERT------------------------------------
        assert uiSolver.leftClicked == True

    def test_UISquareIsRightClickedWithProperties_When_DrawCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed, mock_squareSpace):
        #SETUP------------------------------------------------------
        #mock class args
        mock_viewManager = Mock()
        mock_uiGrid = Mock()

        #grid
        N = go.NOTHING
        W = go.WALL
        S = go.SOLVER
        G = go.GOAL
        P = go.PATH
        F = go.FINDER
        currentGrid = [
                [G, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                                        ]

        #draw function args
        mouseX = 161
        mouseY = 61
        gridRow = 0
        square = 0
        currentGridIndex = 0
        currentGridObject = go.WALL
        pastGrids = []
        mock_pygameMouseGetPressed.return_value = [0, 0, 1]
        mock_squareSpace.collidepoint.return_value = True

        #button class
        uiSolver = UISolver(mock_uiGrid)

        #WORK-------------------------------------
        uiSolver.ClickGrid(mouseX, mouseY, gridRow, square, mock_squareSpace, currentGridIndex, currentGridObject, currentGrid, pastGrids)

        #ASSERT------------------------------------
        assert uiSolver.rightClicked == True

    #Unclick-------------------------------
    def test_UISquareIsLeftUnclickedWithProperties_When_DrawCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed, mock_squareSpace):
        #SETUP------------------------------------------------------
        #mock class args
        mock_viewManager = Mock()
        mock_uiGrid = Mock()

        #grid
        N = go.NOTHING
        W = go.WALL
        S = go.SOLVER
        G = go.GOAL
        P = go.PATH
        F = go.FINDER
        currentGrid = [
                [G, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                                        ]
        
        #button class
        uiSolver = UISolver(mock_uiGrid)
        
        #draw function args
        pastGrids = []
        mock_pygameMouseGetPressed.return_value = [0, 0, 0]
        uiSolver.leftClicked = True
        uiSolver.rightClicked = False

        

        #WORK-------------------------------------
        uiSolver.UnclickGrid(pastGrids, currentGrid, [])

        #ASSERT------------------------------------
        assert uiSolver.leftClicked == False

    def test_UISquareIsRightUnclickedWithProperties_When_DrawCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed, mock_squareSpace):
        #SETUP------------------------------------------------------
        #mock class args
        mock_viewManager = Mock()
        mock_uiGrid = Mock()

        #grid
        N = go.NOTHING
        W = go.WALL
        S = go.SOLVER
        G = go.GOAL
        P = go.PATH
        F = go.FINDER
        currentGrid = [
                [G, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                                        ]
        
        #button class
        uiSolver = UISolver(mock_uiGrid)
        
        #draw function args
        pastGrids = []
        mock_pygameMouseGetPressed.return_value = [0, 0, 0]
        uiSolver.leftClicked = False
        uiSolver.rightClicked = True

        

        #WORK-------------------------------------
        uiSolver.UnclickGrid(pastGrids, currentGrid, [])

        #ASSERT------------------------------------
        assert uiSolver.rightClicked == False


if __name__ == "__main__":
  unittest.main()