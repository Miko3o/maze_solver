class player_stats:
  def __init__(self, health, attack, defense, weapon, armor, inventory):
    self.health = health
    self.attack = attack
    self.defense = defense
    self.weapon = weapon
    self.armor = armor
    self.inventory = inventory

  def Attack():
    print("hi")

class enemy_stats:
  def __init__(self, health, attack, attack_name):
    self.health = health
    self.attack = attack
    self.attack_name = attack_name

  def Attack():
    print("hi")

player = player_stats(100, 5, 10, None, None, None)