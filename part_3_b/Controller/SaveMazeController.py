import csv
import os


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
      writer.writerow([currentGrid, gridSize])
