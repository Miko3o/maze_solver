from Dictionaries_for_Items_and_Enemies import enemies
from Enemy import Enemy
import random


def roll_for_enemy():
  current_enemyid = random.choice(list(enemies))
  enemy = Enemy(enemies[current_enemyid]["name"], enemies[current_enemyid]["health"], enemies[current_enemyid]["attack"], enemies[current_enemyid]["attack_name"])
  print('A', enemy.name, 'appeared!\nHealth:', enemy.health)
  return enemy
