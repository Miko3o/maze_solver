import csv
import tkinter as tk
from tkinter import filedialog
import ast

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
        loadedGrid = ast.literal_eval(row[0]) #trying to convert this string to a regular list but not working atm
        loadedGridSize = int(row[1])
        break
    print("loadedGrid:", loadedGrid)
    print("loadedGridSize:", loadedGridSize)

    #changing grid data
    self.viewManager.modelManager.gridMetaData.ChangeGridData(loadedGrid, loadedGridSize, False, False)
      

