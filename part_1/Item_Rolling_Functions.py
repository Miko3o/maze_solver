from Dictionaries_for_Items_and_Enemies import items
from Weapon import Weapon
from Armor import Armor
import random

def roll_for_armor(player, armor, gameManager):
  print("Rolling for armor")
  armorData = random.choice(list(items["armor"]))
  newArmor = Armor(items["armor"][armorData]["name"], items["armor"][armorData]["defense"])
  gameManager.setArmor(newArmor)
  player.defense = 10
  player.defense += newArmor.defense
  print("Your new armor is:", newArmor.name,"!\n")
  return

def roll_for_weapon(player, weapon, gameManager):
  print("Rolling for armor")
  weaponData = random.choice(list(items["weapons"]))
  newWeapon = Weapon(items["weapons"][weaponData]["name"], items["weapons"][weaponData]["attack"])
  gameManager.setWeapon(newWeapon)
  player.attack = 5
  player.attack += newWeapon.attack
  print("Your new weapon is:", newWeapon.name,"!\n")
  return