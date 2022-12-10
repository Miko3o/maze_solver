import pytest
from unittest.mock import MagicMock, patch
from Controller.NewMazeController import NewMazeController





def test_NewMazeIsCreated_When_NewMazeCalled():
  #setup
  newMazeController = NewMazeController()
  N = "nothing"
  W = "wall"
  currentGrid = [
                [W, W, W, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, N, N, N, N],
                                        ]
  
  
  #work
  currentGrid = newMazeController.NewMaze()

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