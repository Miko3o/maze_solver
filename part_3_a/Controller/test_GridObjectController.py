import pytest
from unittest.mock import MagicMock, patch
from Controller.GridObjectController import GridObjectController


  
#Place---------------------------------------
  
@pytest.mark.xfail
def test_SolverIsPlaced_When_PlaceCalled_WithArg_Solver():
  #setup
  gridObjectController = GridObjectController()
  gridObject = "solver"
  N = "nothing"
  S = "solver"
  
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

    
  currentMousePosition = (currentGrid[0][0], currentGrid[0])


  
  #work
  currentGrid = gridObjectController.Place((currentMousePosition, gridObject))
  
  #assert
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

@pytest.mark.xfail
def test_IndicatedThatSolverIsPlaced_When_PlaceCalled():
  #setup
  gridObjectController = GridObjectController()
  gridObject = "solver"
  N = "nothing"
  
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

    
  currentMousePosition = (currentGrid[0][0], currentGrid[0])


  
  #work
  gridObjectController.Place((currentMousePosition, gridObject))

  #assert
  assert gridObjectController.solverPlaced == True


#Move------------------------------------------

@pytest.mark.xfail
def test_InMovingMode_When_MoveCalled_With_ArgSolver():
  #setup
  gridObjectController = GridObjectController()
  movingMode = False
     
  #work
  gridObjectController.Move()

  #assert
  assert movingMode == True

@pytest.mark.xfail
def test_SolverIsRemoved_When_MovingModeIsTrue():
  #setup
  gridObjectController = GridObjectController()
  gridObject = "solver"
  N = "nothing"
  
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
  gridObjectController.Move(gridObject)

  #assert
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
  

#Add--------------------------------------------

@pytest.mark.xfail
def test_WallIsAdded_When_AddCalled():
  #setup
  gridObjectController = GridObjectController()
  N = "nothing"
  W = "wall"
  
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

    
  currentMousePosition = (currentGrid[0][0], currentGrid[0])


  #work
  currentGrid = gridObjectController.Add((currentMousePosition))
  
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

#Remove-----------------------------------------------------

@pytest.mark.xfail
def test_WallIsRemoved_When_RemoveCalled():
  #setup
  gridObjectController = GridObjectController()
  N = "nothing"
  W = "wall"
  
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

    
  currentMousePosition = (currentGrid[0][0], currentGrid[0])


  #work
  currentGrid = gridObjectController.Remove((currentMousePosition))
  
  #assert
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

#ChangeGridObject------------------------------------------------

@pytest.mark.xfail
def test_GridObjectIsChanged_When_ChangeGridObjectCalled():
  #setup
  gridObjectController = GridObjectController()
  currentGridObject = "solver"

  #work
  currentGridObject = gridObjectController.ChangeGridObject("wall")

  #assert
  assert currentGridObject == "wall"


#GetAllGridObjects----------UNFINISHED------(for the dropdown)
@pytest.mark.xfail
def test_GridObjects():
  #setup
  gridObjectController = GridObjectController()
  print("wip")