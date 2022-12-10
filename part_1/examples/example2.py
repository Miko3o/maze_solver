from enum import Enum, auto

class BattleState(Enum):
  IN_BATTLE = auto()
  NOT_IN_BATTLE = auto()
  DEATH = auto()

class BattleState_Container:
  def __init__(self, battleState):
    self.battleState = battleState

  def SetBattleState(self, new_state):
    self.battleState = new_state

######################################################################
#here's our example

#This doesn't work
def changeStateToInBattle(battleState_pointer):
  battleState_pointer = BattleState.IN_BATTLE #Don't assign arguments to new things

#This works
def changeStateToInBattle_fixed(battleStateContainer_pointer):
  battleStateContainer_pointer.SetBattleState(BattleState.IN_BATTLE) #Notice how we aren't assigning the argument to something new. We are just calling the argument's method to change it

########################################################################
print("Attempt 1 (Doesn't Work)")
  
#Step 1. Set up our State to NOT_IN_BATTLE
state = BattleState.NOT_IN_BATTLE
print("We are not in battle")
print(state)

#Step 2. Set our State to IN_BATTLE
print("\"Setting\" to IN_BATTLE")
changeStateToInBattle(state) #supposed to be IN_BATTLE

#Step 3. Our state should be IN_BATTLE but it's not
print(state)
print("What the???\n\n")

########################################################################
print("Attempt 2")

#Step 1. Set up our State to NOT_IN_BATTLE
state2 = BattleState_Container(BattleState.NOT_IN_BATTLE)
print("We are not in battle")
print(state2.battleState)

#Step 2. Set our State to IN_BATTLE
print("\"Setting\" to IN_BATTLE")
changeStateToInBattle_fixed(state2) #suppoed to be IN_BATTLE

#Step 3. Our state should be IN_BATTLE and it is
print(state2.battleState)
print("WOW!!!")