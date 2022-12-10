from Player import Player
from Enemy import Enemy
from Item import Item
from Weapon import Weapon
from Armor import Armor
from GameStateENUM import BattleState as bs, LoopState as ls
from Not_In_Battle_Function import Not_in_Battle
from In_Battle_Function import In_Battle

class GameManager():

  def __init__(self):
    self.player = Player(100, 5, 10, None, None, None)
    self.currentEnemy  = Enemy("name", 10, 10, "attack_name")
    self.latestItem = Item("name")
    self.currentWeapon = Weapon("None", 0)
    self.currentArmor = Armor("None", 0)
    self.gameState = bs.NOT_IN_BATTLE
    self.loopState = ls.IN_GAME
    self.enemy_chosen = False

  def setEnemy(self, enemy):
    self.currentEnemy = enemy;

  def setEnemyChosen(self, enemy_chosen):
    self.enemy_chosen = enemy_chosen

  def setWeapon(self, weapon):
    self.currentWeapon = weapon

  def setArmor(self, armor):
    self.currentArmor = armor
  
  def Init(self):
    print('Welcome to the land of lands! Here you will perfect your fighting skills so that no living man could best you in the ring of honor! Have fun!\n')
    while self.loopState == ls.IN_GAME:
      if self.gameState == bs.NOT_IN_BATTLE: 
        self.gameState = Not_in_Battle(self.player, self.latestItem, self.currentWeapon, self.currentArmor, self.gameState, self);
      elif self.gameState == bs.IN_BATTLE:
        self.gameState = In_Battle(self.player, self.currentEnemy, self.latestItem, self.gameState, self.enemy_chosen, self);
      elif self.gameState == bs.DEATH:
        print("Oh no, looks like you died!\nWould you like to try again?\nY/N?\n")
        while True:
          answer = input("Answer: ")
          if answer == "y" : self.gameState == bs.NOT_IN_BATTLE; break
          if answer == "n" : quit()
          else:
            print("What?")

#this file is an exception :) -krischin