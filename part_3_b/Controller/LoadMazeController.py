import csv
import tkinter as tk
from tkinter import filedialog
from ast import literal_eval
from View.GameStateENUM import GridObjects as go

class LoadMazeController():

  def __init__(self, viewManager):
    self.viewManager = viewManager

  def LoadMaze(self):
    #tkinter setup
    root = tk.Tk()
    root.withdraw()
    
    #ask user to pick file
    filePath = filedialog.askopenfilename(initialdir="Controller\MazeFiles")
    #if user cancles
    if filePath == '':
      return
    print(filePath)

    #getting grid data from selected file
    with open(filePath) as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        print(type(row[0]))
        gridData = literal_eval(row[0])
        print(gridData)
        loadedGrid = self.ConvertStringsToEnums(gridData) #trying to convert this string to a regular list but not working atm
        print(type(loadedGrid))
        print(loadedGrid)
        loadedGridSize = int(row[1])
        break
    print("loadedGrid:", loadedGrid)
    print("loadedGridSize:", loadedGridSize)

    #changing grid data
    self.viewManager.modelManager.gridMetaData.ChangeGridData(loadedGrid, loadedGridSize, False, False)
      

  def ConvertStringsToEnums(self, gridData):
    for gridRow in range(len(gridData)):
      for gridSquare in range(len(gridData[gridRow])):
        if gridData[gridRow][gridSquare] == "N":
          gridData[gridRow][gridSquare] = go.NOTHING
        elif gridData[gridRow][gridSquare] == "W":
          gridData[gridRow][gridSquare] = go.WALL
        elif gridData[gridRow][gridSquare] == "S":
          gridData[gridRow][gridSquare] = go.SOLVER
        elif gridData[gridRow][gridSquare] == "G":
          gridData[gridRow][gridSquare] = go.GOAL
    return gridData