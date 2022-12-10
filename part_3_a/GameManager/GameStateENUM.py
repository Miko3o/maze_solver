from enum import Enum, auto

class GameState(Enum):
  CREATING_MAZE = auto()
  PICKING_SOLVING_ALG = auto()
  SORTING_SOLVED_MAZE = auto()
  PICKING_SORTING_ALG = auto()
  CLOSING_APP = auto()
  
class LoopState(Enum):
  IN_APP = auto()
  NOT_IN_APP = auto()