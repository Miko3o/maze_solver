from Not_In_Battle_Switch_Functions import switch_choice_1, switch_choice_2, switch_choice_3, switch_choice_4, switch_choice_5
from What_Function import Not_In_Battle_What

def Not_in_Battle(player, item, weapon, armor, gameState, gameManager):
  while True:
    answer = input('What would you like to do?\n1.Battle\n2.Stats and Equipment.\n3.Inventory\n4.Roll for Weapon\n5.Roll for Armor\nAnswer: \n')
    choice = GameState_Switch(answer)
    new_state = choice.__call__(player, item, weapon, armor, gameState, gameManager)
    return new_state
    
def GameState_Switch(answer):
  switcher = {
    "1": switch_choice_1,
    "2": switch_choice_2,
    "3": switch_choice_3,
    "4": switch_choice_4,
    "5": switch_choice_5
  }
  return switcher.get(answer, Not_In_Battle_What)