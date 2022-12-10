import pytest
from unittest.mock import MagicMock, patch
from Controller.GravityController import GravityController


#Gravity----------------------------------------

@pytest.mark.xfail
def test_BlocksAreFallen_When_GravityControllerCalled():
  #setup
  gravityController = GravityController()
  N = "nothing"
  W = "wall"
  
  currentGrid = [
                [W, N, N, N, N, N, W, N],
                [W, N, N, N, N, N, N, N],
                [N, N, N, N, W, N, N, N],
                [N, N, N, N, N, N, W, N],
                [N, N, N, N, W, N, N, N],
                [N, N, N, N, N, N, N, N],
                [N, N, N, N, W, N, N, N],
                [N, N, N, N, N, N, N, N],
                                        ]

  #work
  currentGrid = gravityController.Gravity()

  #assert
  assert currentGrid == [
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, N, N, N, N],
                        [N, N, N, N, W, N, N, N],
                        [W, N, N, N, W, N, W, N],
                        [W, N, N, N, W, N, W, N],
                                                ]