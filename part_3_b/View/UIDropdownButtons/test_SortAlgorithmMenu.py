import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from View.UIDropdownButtons.SortAlgorithmMenu import SortAlgorithmMenu


#Draw------------------------------------------------
@patch("pygame.mouse.get_pressed")
@patch("pygame.Surface")
@patch("pygame.font.SysFont")
@patch("pygame.draw.lines")
@patch("pygame.draw.rect")
class Test_SortAlgorithmMenu(unittest.TestCase):
    def test_MenuIsDrawnWithProperties_When_DrawCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed):
        #SETUP------------------------------------------------------
        #mock class args
        mock_viewManager = Mock()

        #button properties args
        menuColor = (255, 255, 255)
        menuText = ["Bubble Sort", "Intersection Sort", "Merge Sort", "Quick Sort", "Radix Sort", "Selection Sort"]
        menuReturn = ["sra.BubbleSort", "sra.IntersectionSort", "sra.MergeSort", "sra.QuickSort", "sra.RadixSort", "sra.SelectionSort"]
        menuWidth = 150
        menuHeight = 40
        displayX = 5
        displayY = 160
        previousTextHeight = 0
        previousTextSpacing = 0

        #draw function args
        mouseX = 53
        mouseY = 120

        #button class
        sortAlgorithmMenu = SortAlgorithmMenu(mock_pygameSurface, mock_viewManager, menuText, menuReturn, menuWidth, menuHeight, displayX, displayY)

        #WORK-------------------------------------
        sortAlgorithmMenu.Draw(mouseX, mouseY)

        #ASSERT------------------------------------
        mock_pygameDrawRect.assert_called_with(mock_pygameSurface, menuColor, [displayX, 260, menuWidth, 17])

    #Unclick-----------------------------------------------
    def test_MenuIsUnclickedWithProperties_When_DrawCalled(self, mock_pygameDrawRect, mock_pygameDrawLines, mock_pygameFontSysFont, mock_pygameSurface, mock_pygameMouseGetPressed):
        #SETUP------------------------------------------------------
        #mock class args
        mock_viewManager = Mock()

        #button properties args
        menuColor = (255, 255, 255)
        menuText = ["Bubble Sort", "Intersection Sort", "Merge Sort", "Quick Sort", "Radix Sort", "Selection Sort"]
        menuReturn = ["sra.BubbleSort", "sra.IntersectionSort", "sra.MergeSort", "sra.QuickSort", "sra.RadixSort", "sra.SelectionSort"]
        menuWidth = 150
        menuHeight = 40
        displayX = 5
        displayY = 160
        previousTextHeight = 0
        previousTextSpacing = 0

        #draw function args
        mouseX = 53
        mouseY = 121
        mock_pygameMouseGetPressed.return_value = [0]

        #button class
        sortAlgorithmMenu = SortAlgorithmMenu(mock_pygameSurface, mock_viewManager, menuText, menuReturn, menuWidth, menuHeight, displayX, displayY)
        sortAlgorithmMenu.clicked = True

        #WORK-------------------------------------
        sortAlgorithmMenu.UnclickOption(mouseX, mouseY)

        #ASSERT------------------------------------
        assert sortAlgorithmMenu.clicked == False



if __name__ == "__main__":
  unittest.main()