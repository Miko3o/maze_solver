import random

class Player():
 
  def __init__(self, health, attack, defense, weapon, armor, inventory):
    self.health = health
    self.attack = attack
    self.defense = defense
    self.weapon = weapon
    self.armor = armor
    self.inventory = inventory

    #player = Player(100, 5, 10, None, None, None)

  def Attack(self, enemy):
    crit = int(round(random.uniform((self.attack)*0.8, ((self.attack)*1.2))))
    enemy.health -= crit
    print("You attacked the", enemy.name, "for", crit, "damage!\nHealth:", enemy.health, "\n")
    return

#add enemy death conditional