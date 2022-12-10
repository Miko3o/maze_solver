import pytest
from unittest.mock import MagicMock, patch
from UIGrid import UIGrid


#Draw--------------------------------------------

# @pytest.fixture(autouse=True)
# def mock_Surface(mock_Surface):
#   #everything above this yield is called before the test
#   return mock_Surface
  
@patch("pygame.Surface")
def test_CreatesSurface_When_Instantiated(mock_Surface):
  uiGrid =UIGrid()
  assert mock_Surface.called #test that we made the surface with pygame


@patch("pygame.Surface")
def test_CreatesSurface_With_280by280(mock_Surface):
  #setup
  uiGrid = UIGrid()
  mock_Surface.assert_called_with((280,280))

@pytest.mark.skip(reason="Haven't figured out pygame stuff yet")
@patch("pygame.Surface")
def test_BackgroundFilled_With_Color240by240by240(mock_Fill):
  UIGrid().Draw()
  mock_Fill.assert_called_with((240, 240, 240))

