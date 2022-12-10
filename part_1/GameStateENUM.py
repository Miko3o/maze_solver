from enum import Enum, auto

class BattleState(Enum):
  IN_BATTLE = auto()
  NOT_IN_BATTLE = auto()
  DEATH = auto()
  
class LoopState(Enum):
  IN_GAME = auto()
  NOT_IN_GAME = auto()