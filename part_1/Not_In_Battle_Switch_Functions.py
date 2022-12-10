from Item import Item
from Item_Rolling_Functions import roll_for_armor, roll_for_weapon
from GameStateENUM import BattleState as bs, LoopState as ls

def switch_choice_1(player, item, weapon, armor, gameState, gameManager):
  
  return bs.IN_BATTLE
  
def switch_choice_2(player, item, weapon, armor, gameState, gameManager):
  print("Here are your stats:\nHealth: ", player.health, "\nAttack: ", player.attack, "\nDefense: ", player.defense, "\nCurrent Weapon: ", weapon.name, "\nCurrent Armor: ", armor.name, "\n", "hi")
  return bs.NOT_IN_BATTLE

def switch_choice_3(player, item, weapon, armor, gameState, gameManager):
  print(Item.Inventory)
  return bs.NOT_IN_BATTLE

def switch_choice_4(player, item, weapon, armor, gameState, gameManager):
  roll_for_weapon(player, weapon, gameManager)
  return bs.NOT_IN_BATTLE

def switch_choice_5(player, item, weapon, armor, gameState, gameManager):
  roll_for_armor(player, armor, gameManager)
  return bs.NOT_IN_BATTLE

def what(player, item, weapon, armor, gameState, gameManager):
  print("What?")
  return bs.NOT_IN_BATTLE