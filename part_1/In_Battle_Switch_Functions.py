from Player import Player
from Enemy import Enemy
from Item import Item
from Victory_Rolling_Function import roll_for_item
from Dictionaries_for_Items_and_Enemies import enemies, items
from GameStateENUM import BattleState as bs, LoopState as ls


def switch_choice_1(player, enemy, item, gameState, enemy_chosen, gameManager):
    player.Attack(enemy)  #using an object method (object pointer is assumed)
    Enemy.Attack(
        player,
        enemy)  #using a class method (requires a pointer to the object)
    if player.health < 0:
        return bs.DEATH
    else:
        if enemy.health < 0:
            roll_for_item(player, enemy, item, gameState, enemy_chosen, gameManager)
            return bs.NOT_IN_BATTLE
        else:
            return bs.IN_BATTLE


def switch_choice_2(player, enemy, item, gameState, enemy_chosen, gameManager):
    print("You are defending the enemy's attack!\n")
    Enemy.Attack(player, enemy)
    return bs.IN_BATTLE


def switch_choice_3(player, enemy, item, gameState, enemy_chosen, gameManager):
    print("You ran away!\n")
    return bs.NOT_IN_BATTLE
