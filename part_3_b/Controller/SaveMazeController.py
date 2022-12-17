import csv
import os
from View.GameStateENUM import GridObjects as go

class SaveMazeController():

  def __init__(self):
    print("wip")

  def SaveMaze(self, currentGrid, gridSize):
    mazeFiles = "Controller\MazeFiles"
    count = 0
    for file in os.listdir(mazeFiles):
      if os.path.isfile(os.path.join(mazeFiles, file)):
        count +=1

    print(count)
    with open('Controller\MazeFiles\maze' + str(count) + '.csv', 'w') as mazeFile:
      writer = csv.writer(mazeFile)
      newGrid = self.ChangeGrid(currentGrid)
      writer.writerow([newGrid, gridSize])

  def ChangeGrid(self, currentGrid):
    for gridRow in range(len(currentGrid)):
      for gridSquare in range(len(currentGrid[gridRow])):
        if currentGrid[gridRow][gridSquare] == go.NOTHING:
          currentGrid[gridRow][gridSquare] = "N"
        elif currentGrid[gridRow][gridSquare] == go.WALL:
          currentGrid[gridRow][gridSquare] = "W"
        elif currentGrid[gridRow][gridSquare] == go.SOLVER:
          currentGrid[gridRow][gridSquare] = "S"
        elif currentGrid[gridRow][gridSquare] == go.GOAL:
          currentGrid[gridRow][gridSquare] = "G"
    return currentGrid
