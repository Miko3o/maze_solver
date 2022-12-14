from View.GameStateENUM import GameState as gs, LoopState as ls, GridObjects as go, SolvingAlgorithm as sa, SortingAlgorithm as sra
import pygame
from sys import exit

from Controller.ControllerManager import ControllerManager
from Model.ModelManager import ModelManager

from View.UIGrid import UIGrid
from View.UIButtons.UIClearMazeButton import UIClearMazeButton
from View.UIButtons.UIGravityButton import UIGravityButton
from View.UIButtons.UILoadButton import UILoadButton
from View.UIButtons.UIRedoButton import UIRedoButton
from View.UIButtons.UISaveButton import UISaveButton
from View.UIButtons.UISolveButton import UISolveButton
from View.UIButtons.UISortButton import UISortButton
from View.UIButtons.UIUndoButton import UIUndoButton
from View.UIDropdownButtons.SelectGridObjectDropdown import SelectGridObjectDropdown
from View.UIDropdownButtons.SelectGridObjectMenu import SelectGridObjectMenu
from View.UIDropdownButtons.SelectPastGridsDropdown import SelectPastGridsDropdown
from View.UIDropdownButtons.SolveAlgorithmDropdown import SolveAlgorithmDropdown
from View.UIDropdownButtons.SolveAlgorithmMenu import SolveAlgorithmMenu
from View.UIDropdownButtons.SortAlgorithmDropdown import SortAlgorithmDropdown
from View.UIDropdownButtons.SortAlgorithmMenu import SortAlgorithmMenu
from View.UISlider.UIBar import UIBar
from View.UISlider.UISlideSquare import UISlideSquare

pygame.init()

class ViewManager():
  def __init__(self):

    #gamewindow:
    self.gameWindow = pygame.display.set_mode((600, 400))

    #managers:
    self.controllerManager = ControllerManager(self, self.gameWindow)
    self.modelManager = ModelManager(go.NOTHING, go.WALL, go.SOLVER, go.GOAL, go.FINDER, go.PATH)

    

    #UI Objects
    #grid


    self.currentGridObject = go.WALL
    self.uiGrid = UIGrid(self.gameWindow, self, self.currentGridObject)
    
    #UIButtons
    self.uiClearMazeButton = UIClearMazeButton(self.gameWindow, self, [255, 247, 98], (190, 181, 17), "Clear Maze", 180, 30, 260, 17)
    self.uiGravityButton = UIGravityButton(self.gameWindow, self, [226, 128, 241], (150, 54, 165), "GRAVITY", 100, 70, 472, 150)
    self.uiLoadButton = UILoadButton(self.gameWindow, self, [158, 234, 255], (18, 58, 142), "Load", 75, 30, 30, 17)
    self.uiRedoButton = UIRedoButton(self.gameWindow, self, [125, 255, 203], (56, 128, 93,), ">", 30, 30, 540, 17)
    self.uiSaveButton = UISaveButton(self.gameWindow, self, [255, 150, 173], (139, 49, 73), "Save", 75, 30, 130, 17)
    self.uiSolveButton = UISolveButton(self.gameWindow, self, [255, 205, 119], (169, 119, 33), "SOLVE", 100, 70, 472, 70)
    self.uiSortButton = UISortButton(self.gameWindow, self, [255, 205, 119], (169, 119, 33), "SORT", 100, 70, 472, 150)
    self.uiUndoButton = UIUndoButton(self.gameWindow, self, [125, 255, 203], (56, 128, 93,), "<", 30, 30, 500, 17)
    
    #DropdownUIButtons
      #Select Object
    self.selectGridObjectDropdown = SelectGridObjectDropdown(self.gameWindow, [230, 230, 230], "Select Object", 120, 30, 30, 80, self)
    self.selectGridObjectMenu = SelectGridObjectMenu(self.gameWindow, self, ["Wall", "Solver", "Goal"], [go.WALL, go.SOLVER, go.GOAL], 70, 30, 52, 120)
      #Select Past Grid
    self.selectPastGridsDropdown = SelectPastGridsDropdown(self.gameWindow, [230, 230, 230], "Select Object", 75, 30, 30, 50, self)
      #Select Solving Algorithm
    self.solveAlgorithmDropdown = SolveAlgorithmDropdown(self.gameWindow, [230, 230, 230], "Pick Algorithm", 120, 30, 30, 230, self)
    self.solveAlgorithmMenu = SolveAlgorithmMenu(self.gameWindow, self, ["BFS", "DFS", "Dijkstra", "A*"], [sa.BFS, sa.DFS, sa.Dijkstra, sa.Astar], 80, 40, 47, 270)
      #Select Sort Algorithm
    self.sortAlgorithmDropdown = SortAlgorithmDropdown(self.gameWindow, [230, 230, 230], "Pick Algorithm", 120, 30, 30, 120, self)
    self.sortAlgorithmMenu = SortAlgorithmMenu(self.gameWindow, self, ["Bubble Sort", "Intersection Sort", "Merge Sort", "Quick Sort", "Radix Sort", "Selection Sort"], [sra.BubbleSort, sra.IntersectionSort, sra.MergeSort, sra.QuickSort, sra.RadixSort, sra.SelectionSort], 150, 40, 5, 160)

    #Slider
    self.uiBar = UIBar(self.gameWindow)
    self.uiSlideSquare = UISlideSquare(self.gameWindow)
    self.sliderX = 507

    #UISquares
    #self.uiNothing = UINothing()
    #self.uiWall = UIWall()
    #self.uiSolver = UISolver()
    #self.uiGoal = UIGoal()
    #self.uiFinder = UIFinder()
    #self.uiPath = UIPath()

    #UISquares in Array
    #self.uiSquareList = [self.uiFinder, self.uiGoal, self.uiNothing, self.uiPath, self.uiSolver, self.uiWall]
    
    #clock
    self.clock = pygame.time.Clock()

    #setting states
    self.gameState = gs.CREATING_MAZE
    self.loopState = ls.IN_APP

    #mouse
    self.mouseX = None
    self.mouseY = None

    #button arrays
    self.buttonList = [self.uiLoadButton, self.uiSaveButton, self.uiUndoButton, self.uiRedoButton, self.uiSolveButton, self.uiGravityButton, self.selectGridObjectDropdown, self.solveAlgorithmDropdown]

    #grid info
    self.currentGridData = None
    
    self.currentGridIndex = (3, 3)
    self.placingOnGrid = False
    self.currentSquare = None






  
  def ProgramLoop(self):

    #WHILE IN APP
    while self.loopState == ls.IN_APP:

      #setting up window
      self.gameWindow.fill('White')
      
      #mouse position
      self.mouseX, self.mouseY = pygame.mouse.get_pos()

      #model data
      currentGridDataTuple = self.modelManager.gridMetaData.GetGridData()
      self.currentGridData = list(currentGridDataTuple)

      #states

      ###############CREATING MAZE##################
      
      if self.gameState == gs.CREATING_MAZE:
        #CONTROLLERS
        #changing grid size--------------------
        changeInGridSizeTuple = self.controllerManager.gridController.ResizeGrid(self.sliderX, self.currentGridData[0], self.currentGridData[1])
        
        changeInGridSize = list(changeInGridSizeTuple)

    
        #drawing buttons grid, and slider--------------
        self.DrawingButtonsGridAndSliderHandler(self.currentGridData)
        
        #----------------------------------------
        
        #MODEL
        self.modelManager.gridMetaData.ChangeGridData(changeInGridSize[0], changeInGridSize[1], False, False)
        #if self.placingOnGrid == True:
          #self.modelManager.gridMetaData.ChangeGridIndices(self.currentGridIndex, self.currentGridObject)


      ###############SELECTING GRID OBJECT######################
      
      elif self.gameState == gs.SELECTING_GRID_OBJECT:
        #drawing buttons, grid, and slider----------------------------
        self.DrawingButtonsGridAndSliderHandler(self.currentGridData)

        #drawing dropdown menu
        self.selectGridObjectMenu.Draw(self.mouseX, self.mouseY)
        #-----------------------------------------------------
        
      ###################PICKING SOLVING ALGORITHM#################
      
      elif self.gameState == gs.PICKING_SOLVING_ALG:
        #drawing buttons, grid, and slider-------------------------------
        self.DrawingButtonsGridAndSliderHandler(self.currentGridData)

        #drawing dropdown menu
        self.solveAlgorithmMenu.Draw(self.mouseX, self.mouseY)
        #-------------------------------------------------------

      #############SORTING SOLVED MAZE##################

      elif self.gameState == gs.SORTING_SOLVED_MAZE:
        self.DrawingButtonsGridAndSliderHandler(self.currentGridData)

      #############PICKING SORTING ALGORITHM#################
      elif self.gameState == gs.PICKING_SORTING_ALG:
        self.DrawingButtonsGridAndSliderHandler(self.currentGridData)

        #drawing dropdown menu
        self.sortAlgorithmMenu.Draw(self.mouseX, self.mouseY)

      elif self.gameState == gs.CLOSING_APP:
        print("CLOSING_APP: wip")




      ######CLICKING EVENTS########
        
      #events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        #when the mouse is clicked down
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            self.MouseDownHandler()
        #when the finger is released form the mouse
        elif event.type == pygame.MOUSEBUTTONUP:
          if event.button == 1:
            self.MouseUpHandler()
        elif event.type == pygame.MOUSEMOTION:
          self.sliderX = self.uiSlideSquare.DragSquare(self.mouseX, self.mouseY)
      
      #updates the display surface
      pygame.display.update()
      self.clock.tick(60)




  
  
  def MouseDownHandler(self):
    for method in self.buttonList:
      method.ClickButton(self.mouseX, self.mouseY)
    self.uiClearMazeButton.ClickButton(self.mouseX, self.mouseY)
    if self.gameState == gs.SORTING_SOLVED_MAZE or self.gameState == gs.PICKING_SORTING_ALG: 
      self.sortAlgorithmDropdown.ClickButton(self.mouseX, self.mouseY)
      self.uiSortButton.ClickButton(self.mouseX, self.mouseY)



        
    self.uiSlideSquare.ClickButton(self.mouseX, self.mouseY)
    print("mouseDown pos:", self.mouseX, self.mouseY)



  
  def MouseUpHandler(self):
    if self.gameState == gs.CREATING_MAZE or self.gameState == gs.SELECTING_GRID_OBJECT or self.gameState == gs.PICKING_SOLVING_ALG:
      for method in self.buttonList:
        self.gameState = method.UnclickButton(self.currentGridData[0], self.currentGridData[1], self.currentGridData[2], self.currentGridData[3])
        if self.gameState != gs.CREATING_MAZE:
          break
      self.uiClearMazeButton.UnclickButton(self.currentGridData[0], self.currentGridData[1], self.currentGridData[2], self.currentGridData[3], self.gameState)
    if self.gameState == gs.SORTING_SOLVED_MAZE or self.gameState == gs.PICKING_SORTING_ALG:    
      self.sortAlgorithmDropdown.UnclickButton(self.currentGridData[0], self.currentGridData[1], self.currentGridData[2], self.currentGridData[3], self.gameState)
      self.uiClearMazeButton.UnclickButton(self.currentGridData[0], self.currentGridData[1], self.currentGridData[2], self.currentGridData[3], self.gameState)
      self.uiSortButton.UnclickButton(self.currentGridData[0], self.currentGridData[1], self.currentGridData[2], self.currentGridData[3])
    self.sortAlgorithmMenu.UnclickOption(self.mouseX, self.mouseY)
    

    self.selectGridObjectMenu.UnclickOption(self.mouseX, self.mouseY)
    self.solveAlgorithmMenu.UnclickOption(self.mouseX, self.mouseY)
    self.uiSlideSquare.UnclickButton(self.mouseX, self.mouseY)
    #print("mouseUp pos:  ", self.mouseX, self.mouseY)


  

  def DrawingButtonsGridAndSliderHandler(self, currentGridData):
    #drawing buttons and grid--------------
      self.uiGrid.Draw(currentGridData[0], currentGridData[2], self.mouseX, self.mouseY, self.currentGridObject, currentGridData[3])

      if self.gameState == gs.CREATING_MAZE or self.gameState == gs.SELECTING_GRID_OBJECT or self.gameState == gs.PICKING_SOLVING_ALG:
        for method in self.buttonList:
          method.Draw(self.mouseX, self.mouseY)
        self.uiClearMazeButton.Draw(self.mouseX, self.mouseY)

        #drawing slider
        self.uiBar.Draw()
        self.uiSlideSquare.Draw(self.mouseX, self.mouseY)

      if self.gameState == gs.SORTING_SOLVED_MAZE or self.gameState == gs.PICKING_SORTING_ALG:
        self.uiClearMazeButton.Draw(self.mouseX, self.mouseY)
        self.uiSortButton.Draw(self.mouseX, self.mouseY)
        self.sortAlgorithmDropdown.Draw(self.mouseX, self.mouseY)


  def ChangeGridObject(self, changedObject):
    self.currentGridObject = changedObject
    print("currentGridObject:", self.currentGridObject)

  def ChangeGameState(self, changedState):
    self.gameState = changedState
    print("newGameState:", self.gameState)