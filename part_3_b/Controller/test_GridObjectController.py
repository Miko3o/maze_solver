import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
from Controller.GridObjectController import GridObjectController
from View.GameStateENUM import GridObjects as go

#Place---------------------------------------
class Test_GridObjectController(unittest.TestCase):
  def test_SolverIsPlaced_When_PlaceCalled(self):
    #SETUP-----------------------------------
    #mock args
    mock_viewManager = Mock()

    gridObjectController = GridObjectController(mock_viewManager)
    newGridObject = go.SOLVER
    newIndex = (0, 0)
    pastGrids = []
    clickedBool = True
    N = go.NOTHING
    S = go.SOLVER
    
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


    #WORK-------------------------------------
    gridObjectController.Place(newIndex, newGridObject, currentGrid, pastGrids, clickedBool)
    
    #ASSERT----------------------------------
    assert currentGrid == [
                          [S, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                                                  ]

  def test_WallIsAdded_When_PlaceCalled(self):
    #SETUP-----------------------------------
    #mock args
    mock_viewManager = Mock()

    gridObjectController = GridObjectController(mock_viewManager)
    newGridObject = go.WALL
    newIndex = (0, 0)
    pastGrids = []
    clickedBool = True
    N = go.NOTHING
    W = go.WALL
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

    
    #work
    gridObjectController.Place(newIndex, newGridObject, currentGrid, pastGrids, clickedBool)
    
    #assert
    assert currentGrid == [
                          [W, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                                                  ]


  def test_IndicatedThatSolverIsPlaced_When_PlaceCalled(self):
    #SETUP---------------------------------------
    #mock args
    mock_viewManager = Mock()

    gridObjectController = GridObjectController(mock_viewManager)
    newGridObject = go.SOLVER
    newIndex = (0, 0)
    pastGrids = []
    clickedBool = True
    N = go.NOTHING
    S = go.SOLVER
    
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

    
    #WORK------------------------------------------
    gridObjectController.Place(newIndex, newGridObject, currentGrid, pastGrids, clickedBool)

    #ASSERT-------------------------------------
    assert gridObjectController.solverExists == True







  #Remove-----------------------------------------------------

  def test_WallIsRemoved_When_RemoveCalled(self):
    #SETUP---------------------------------------
    #mock args
    mock_viewManager = Mock()

    gridObjectController = GridObjectController(mock_viewManager)
    newGridObject = go.WALL
    newIndex = (0, 0)
    pastGrids = []
    clickedBool = True
    N = go.NOTHING
    W = go.WALL
    
    currentGrid = [
                  [W, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                                          ]


    #WORK------------------------------------
    gridObjectController.Erase(newIndex, newGridObject, currentGrid, pastGrids, clickedBool)
    
    #ASSERT-----------------------------------
    assert currentGrid == [
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                          [N, N, N, N, N, N, N, N],
                                                  ]

  #UnclickToSavePastGrids-----------------------------------
  def test_GridIsSavedToPastGrids_When_UnclickToSavePastGridsCalled(self):
    #SETUP-----------------------------------------------
    #mock args
    mock_viewManager = Mock()

    gridObjectController = GridObjectController(mock_viewManager)
    N = go.NOTHING
    W = go.WALL
    currentGrid = [
                  [W, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                                          ]
    pastGrids = [[
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                  [N, N, N, N, N, N, N, N],
                                          ]]
    currentPastGridsIndex = -1

    #WORK----------------------------------------------
    gridObjectController.UnclickToSavePastGrids(pastGrids, currentGrid, currentPastGridsIndex)
    
    #ASSERT----------------------------------------------
    assert pastGrids == [[
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                                                ], [
                        [W, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                                                ]]
                                                  

if __name__ == "__main__":
  unittest.main()