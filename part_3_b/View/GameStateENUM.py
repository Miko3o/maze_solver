from enum import Enum, auto

class GameState(Enum):
  CREATING_MAZE = auto()
  SELECTING_GRID_OBJECT = auto()
  PICKING_SOLVING_ALG = auto()
  SORTING_SOLVED_MAZE = auto()
  PICKING_SORTING_ALG = auto()
  CLOSING_APP = auto()
  
class LoopState(Enum):
  IN_APP = auto()
  NOT_IN_APP = auto()

class ButtonType(Enum):
  LOAD = auto()
  SAVE = auto()
  UNDO = auto()
  REDO = auto()
  SLIDER = auto()
  SOLVE = auto()
  SORT = auto()
  GRAVITY = auto()
  SELECT_OBJECT = auto()
  PICK_SOLVE_ALG = auto()
  PICK_SORT_ALG = auto()
  


class GridObjects(Enum):
  NOTHING = auto()
  WALL = auto()
  SOLVER = auto()
  GOAL = auto()
  FINDER = auto()
  PATH = auto()

class SolvingAlgorithm(Enum):
  BFS = auto()
  DFS = auto()
  Dijkstra = auto()
  Astar = auto()

class SortingAlgorithm(Enum):
  BubbleSort = auto()
  IntersectionSort = auto()
  MergeSort = auto()
  QuickSort = auto()
  RadixSort = auto()
  SelectionSort = auto()