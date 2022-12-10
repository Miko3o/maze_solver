@pytest.mark.skip(reason="Haven't figured out pygame stuff yet")
@patch("pygame.draw.line")
def test_GridLinesAreInCorrectPosition_When_DrawCalled(mock_DrawLine):

  #setup
  uiGrid = UIGrid()
  # N = "nothing"
  gridBackground = "background" #mock the return value of this -> pygame.Surface((280,280))
  
  # currentGrid = [
  #               [N, N, N, N, N, N, N, N],
  #               [N, N, N, N, N, N, N, N],
  #               [N, N, N, N, N, N, N, N],
  #               [N, N, N, N, N, N, N, N],
  #               [N, N, N, N, N, N, N, N],
  #               [N, N, N, N, N, N, N, N],
  #               [N, N, N, N, N, N, N, N],
  #               [N, N, N, N, N, N, N, N],
  #                                       ]

  # distanceBetweenRows = 280 / len(currentGrid)
  # lineStartPositionx = 0
  # lineStartPositiony = 0
  # gridBackground = "background"

  # work
  # for x in range(currentGrid[0]):
  #   lineStartPositionx += distanceBetweenRows
  #   mock_DrawLine(gridBackground, (0, 0, 0), (lineStartPositionx, 0), (lineStartPositionx, 280))
                  
  #for y in range(currentGrid):
    #lineStartPositiony += distanceBetweenRows
    #mock_DrawLine(gridBackground, (0, 0, 0), (0, lineStartPositiony), (280, lineStartPositiony))
  
  uiGrid.Draw(gridBackground)
  
  #assert
  mock_DrawLine.assert_called_with(gridBackground, (0, 0, 0), (35, 0), (35, 280))