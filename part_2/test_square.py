import pytest

class GridTestSuite:

  #==================Test Driven Development========================================
  
  #Does the class render a 16x16 grid?
  def test_rendersGrid():
    #set a grid
    
    assert False

  #Does the grid contain Square Objects?
  def test_containsSquareObjects():
    #set a grid
    
    assert False

  #Can the grid be cleared with a single function?
  def test_gridClear():
    #set a grid
    
    assert False
    
  #Can the user click on a square on the grid and change the color of the square?
  def test_gridClick():
    assert False

  #Does the grid spawn a "solver" object?
  def test_hasSolver():
    assert False

  #Does the grid solve an empty maze?
  def test_solveEmptyMaze():
    assert False

  #Does the grid solve a partial maze?
  def test_solvePartialMaze():
    assert False

  #Does the grid fail on a completely filled maze?
  def test_failFullMaze():
    assert False


  #=================QA Testing ============================================================
  #Does the grid return an error if negative dimensions are passed into the constructor?
  def test_negativeGrid():
    try:
      grid = Grid(-16, -16)
      assert False #test fails
    except:
      assert True #test passes

  #Does the grid return an error if a string is passed into the constructor?
  def test_stringGrid():
    try:
      grid = Grid("16", "16")
      assert False
    except: #if an error was thrown
      assert True #test passes

  #Does the grid return a grid?
  def test_grid():
    try:
      grid = Grid(1,1)
      assert grid != None
    except:
      assert False