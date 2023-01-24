import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from View.UIGrid import UIGrid
from View.GameStateENUM import GridObjects as go


#Draw--------------------------------------------
@patch("View.UIGrid.UIGrid.DrawLinesHandler")
@patch("View.UIGrid.UIGrid.DrawSquaresHandler")
@patch("pygame.mouse.get_pressed")
@patch("pygame.Surface")
@patch("pygame.font.SysFont")
@patch("pygame.draw.lines")
@patch("pygame.draw.rect")
class Test_UIGrid(unittest.TestCase):
  def test_UIGridBackgroundIsDrawnWithProperties_When_DrawCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed, mock_drawSquaresHandler, mock_drawLinesHandler):
    #SETUP------------------------------------------------------
    #mock class args
    mock_viewManager = Mock()

    #grid class
    uiGrid = UIGrid(mock_pygameSurface, mock_viewManager, go.WALL)

    #grid
    N = go.NOTHING
    W = go.WALL
    S = go.SOLVER
    G = go.GOAL
    P = go.PATH
    F = go.FINDER
    currentGrid = [
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                                          ]
    
    #function args
    pastGrids = []
    mouseX = 0
    mouseY = 0
    currentGridObject = go.WALL
    currentPastGridsIndex = 0
    
    #WORK------------------------------------------------
    uiGrid.Draw(currentGrid, pastGrids, mouseX, mouseY, currentGridObject, currentPastGridsIndex)

    #ASSERT---------------------------------------------
    mock_pygameDrawRect.assert_called_with(mock_pygameSurface, (240, 240, 240), [160, 60, 280, 280])

  def test_UIGridLinesIsDrawnWithProperties_When_DrawCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed, mock_drawSquaresHandler, mock_drawLinesHandler):
    #SETUP------------------------------------------------------
    #mock class args
    mock_viewManager = Mock()

    #grid class
    uiGrid = UIGrid(mock_pygameSurface, mock_viewManager, go.WALL)

    #grid
    N = go.NOTHING
    W = go.WALL
    S = go.SOLVER
    G = go.GOAL
    P = go.PATH
    F = go.FINDER
    currentGrid = [
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                                          ]
    
    #function args
    pastGrids = []
    mouseX = 0
    mouseY = 0
    currentGridObject = go.WALL
    currentPastGridsIndex = 0
    
    #WORK------------------------------------------------
    uiGrid.DrawSquaresHandler(160, 60, 35, currentGrid, go.WALL)

    #ASSERT---------------------------------------------
    mock_pygameDrawLines.assert_called

  def test_UIGridIsClicked_When_DrawCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed, mock_drawSquaresHandler, mock_drawLinesHandler):
    #SETUP------------------------------------------------------
    #mock class args
    mock_viewManager = Mock()

    #grid class
    uiGrid = UIGrid(mock_pygameSurface, mock_viewManager, go.WALL)

    #grid
    N = go.NOTHING
    W = go.WALL
    S = go.SOLVER
    G = go.GOAL
    P = go.PATH
    F = go.FINDER
    currentGrid = [
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                                          ]
    
    #function args
    pastGrids = []
    mouseX = 0
    mouseY = 0
    mock_pygameMouseGetPressed.return_value = [1]
    uiGrid.clicked = False
    uiGrid.gridSquareClicked = True
    
    #WORK------------------------------------------------
    uiGrid.ClickGrid(mouseX, mouseY)

    #ASSERT---------------------------------------------
    uiGrid.clicked == True

  def test_UIGridIsUnclicked_When_DrawCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed, mock_drawSquaresHandler, mock_drawLinesHandler):
    #SETUP------------------------------------------------------
    #mock class args
    mock_viewManager = Mock()

    #grid class
    uiGrid = UIGrid(mock_pygameSurface, mock_viewManager, go.WALL)

    #grid
    N = go.NOTHING
    W = go.WALL
    S = go.SOLVER
    G = go.GOAL
    P = go.PATH
    F = go.FINDER
    currentGrid = [
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                                          ]
    
    #function args
    pastGrids = []
    mouseX = 0
    mouseY = 0
    mock_pygameMouseGetPressed.return_value = [0]
    uiGrid.clicked = True
    
    #WORK------------------------------------------------
    uiGrid.ClickGrid(mouseX, mouseY)

    #ASSERT---------------------------------------------
    uiGrid.clicked == False

if __name__ == "__main__":
  unittest.main()

