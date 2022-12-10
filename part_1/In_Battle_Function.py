from Item import Item
from Enemy_Rolling_Functions import roll_for_enemy
from GameStateENUM import BattleState as bs, LoopState as ls
from In_Battle_Switch_Functions import switch_choice_1, switch_choice_2, switch_choice_3
from What_Function import In_Battle_What

def In_Battle(player, enemy, item, gameState, enemy_chosen, gameManager):
  if enemy_chosen == False:
    gameManager.setEnemy(roll_for_enemy());
    gameManager.setEnemyChosen(True)
  while True:
    answer = input('What do you do?\n1.Attack\n2.Defend.\n3.Run\nAnswer: \n')
    choice = GameState_Switch(answer)
    new_state = choice.__call__(player, gameManager.currentEnemy, item, gameState, gameManager.enemy_chosen, gameManager)
    if new_state == bs.NOT_IN_BATTLE:
      gameManager.setEnemyChosen(False)
    return new_state

def GameState_Switch(answer):
  switcher = {
    "1": switch_choice_1,
    "2": switch_choice_2,
    "3": switch_choice_3,
  }
  return switcher.get(answer, In_Battle_What)
