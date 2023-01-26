from View.GameStateENUM import GridObjects as go
import copy


class GridObjectController():

  def __init__(self, viewManager):
    self.viewManager = viewManager
    self.currentGrid = []
    self.pastGrids = []
    
    self.solverExists = False
    self.goalExists = False

    self.currentGridObject = go.WALL

    self.clicked = False

  def Place(self, newIndex, newGridObject, currentGrid, pastGrids, clickedBool):
    self.currentGrid = currentGrid
    self.clicked = clickedBool
    newIndexList = list(newIndex)
    if newGridObject == go.WALL:
      self.currentGrid[newIndexList[0]][newIndexList[1]] = go.WALL
    elif newGridObject == go.SOLVER:
      self.solverExists = self.PlaceOneTimeOnlyHandler(newIndexList, go.SOLVER, self.solverExists)
    elif newGridObject == go.GOAL:
      self.goalExists = self.PlaceOneTimeOnlyHandler(newIndexList, go.GOAL, self.goalExists)

      

  def Erase(self, newIndex, newGridObject, currentGrid, pastGrids, clickedBool):
    self.currentGrid = currentGrid
    self.clicked = clickedBool
    newIndexList = list(newIndex)
    if newGridObject == go.WALL:
      self.currentGrid[newIndexList[0]][newIndexList[1]] = go.NOTHING
    elif newGridObject == go.SOLVER and self.solverExists == True and self.currentGrid[newIndexList[0]][newIndexList[1]] == go.SOLVER:
      self.currentGrid[newIndexList[0]][newIndexList[1]] = go.NOTHING
      self.solverExists = False
    elif newGridObject == go.GOAL and self.goalExists == True and self.currentGrid[newIndexList[0]][newIndexList[1]] == go.GOAL:
      self.currentGrid[newIndexList[0]][newIndexList[1]] = go.NOTHING
      self.goalExists = False

  def UnclickToSavePastGrids(self, pastGrids, currentGrid, currentPastGridsIndex):
    #STEP 1: check if mouse is clicked
    if self.clicked == True:
      #STEP 2: get the range of the end of the pastGrids array and the current Index
      realIndex = self.ConvertIndexToPositiveNumberHandler(pastGrids, currentPastGridsIndex)
      rangeBetweenPastGridsIndexAndLength = len(pastGrids) - realIndex
      #STEP 3: append a copy of the current grid to the pastGrids array
      copyGrid = copy.deepcopy(currentGrid)
      pastGrids.append(copyGrid)   
      print("rangeBetweenPastGridsIndexAndLength:", rangeBetweenPastGridsIndexAndLength)
      print("old pastGrids length:", len(pastGrids))
      #STEP 4: if the current index is not at the end of the past array index, delete all the indecies ahead of it
      if rangeBetweenPastGridsIndexAndLength != 0:
        for i in range(rangeBetweenPastGridsIndexAndLength):
          pastGrids.pop()
          print("pop")
      print("new pastGrids length:", len(pastGrids))
      currentPastGridsIndex = -1
      print("pastGrids index:", currentPastGridsIndex)
      print("realIndex:", realIndex)
    self.viewManager.modelManager.gridMetaData.ChangeGridData(self.currentGrid, False, pastGrids, currentPastGridsIndex)

  def ConvertIndexToPositiveNumberHandler(self, pastGrids, currentPastGridsIndex):
    #example: if grid length is 5, index -1 becomes 4
    print("currentPastGridsIndex:", currentPastGridsIndex)
    realIndex = currentPastGridsIndex % len(pastGrids)
    return realIndex + 1



  #HANDLERS---------------------------------------------------------------
  def PlaceOneTimeOnlyHandler(self, newIndexList, gridObject, existCondition):
    for gridRow in range(len(self.currentGrid)):
      for square in range(len(self.currentGrid[gridRow])):
        if self.currentGrid[gridRow][square] == gridObject:
          return True
    self.currentGrid[newIndexList[0]][newIndexList[1]] = gridObject
    return True