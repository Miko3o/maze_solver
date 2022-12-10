import pytest
from unittest.mock import MagicMock, patch
from View.ViewManager import ViewManager
from GameManager import GameManager

@pytest.mark.skip(reason="deal with this later")
@patch("pygame.display.set_mode")
def test_GameWindowIsCreated_When_Instantiated(mock_SetDisplay):
  GameManager()
  assert mock_SetDisplay.called

@pytest.mark.skip(reason="deal with this later")
@patch("pygame.display.set_mode")
def test_GameWindowIsCreated_With_Demensions600by400(mock_SetDisplay):
  GameManager()
  mock_SetDisplay.assert_called_with((600, 400))

@pytest.mark.skip(reason="We don't know how to mock a class by itself")
@patch("View.ViewManager.ViewManager.__init__")
@patch("pygame.display.set_mode")
def test_ViewManagerIsInstantiated_With_GameWindow(mock_gameWindow, mock_ViewManagerConstructor):
  gameManager = GameManager()
  mock_ViewManager = mock_ViewManagerConstructor.return_value
  assert gameManager.viewManager == mock_ViewManager