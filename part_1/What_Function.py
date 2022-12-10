from GameStateENUM import BattleState as bs

def Not_In_Battle_What(player, item, weapon, armor, gameState, gameManager):
  print("What?")
  return bs.NOT_IN_BATTLE

def In_Battle_What(player, enemy, item, gameState, enemy_chosen, gameManager):
  print("What?")
  return bs.IN_BATTLE
