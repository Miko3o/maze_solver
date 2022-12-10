from Dictionaries_for_Items_and_Enemies import enemies
import random

class Enemy:
  def __init__(self, name, health, attack, attack_name):
    self.name = name
    self.health = health
    self.attack = attack
    self.attack_name = attack_name

  def Attack(player, enemy):
    player.health -= (enemy.attack - player.defense)
    print("The", enemy.attack_name, "\nThe", enemy.name, "attacked you for", enemy.attack - player.defense, "damage!\nYour Health:", player.health, "\n")
    return

