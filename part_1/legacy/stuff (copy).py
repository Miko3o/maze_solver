import random
import classroom
inventory = []
named_inventory = []
multiple_value_item = None

def set_variables():
  global enemy_chosen
  global current_weaponid
  global current_armorid
  global current_enemyid
  global current_itemid
  global multiple_value_item
  global dead
  enemy_chosen = False
  current_weaponid = 0
  current_armorid = 8
  current_enemyid = None
  multiple_value_item = None
  current_itemid = None
  player.health = 100
  dead = False
  get_choice_1()

player = classroom.player_stats(100, 5, 10, None, None, None)

#choices

def get_choice_1():
  while True:
    answer = input('What would you like to do?\n1.Battle\n2.Stats and Equipment.\n3.Inventory\n4.Roll for Weapon\n5.Roll for Armor\nAnswer: ')
    if answer == "1" :
      attack_choice()
      break
    if answer == "2" :
      check_stats()
      get_choice_1()
    if answer == "3" :
      access_inventory()
      get_choice_1()
    if answer == "4" : roll_for_weapon(items["weapons"])
    if answer == "5" : roll_for_armor(items["armor"])
    else:
      print("What?")

def choice_attack():
  global enemy_chosen
  global dead
  while True:
             
    #you are attacking    

    crit = int(round(random.uniform(((classroom.player.attack) + (items["weapons"][current_weaponid]["attack"]))*0.8, (((classroom.player.attack) + (items["weapons"][current_weaponid]["attack"]))*1.2))))
    enemy.health = (enemy.health) - crit
    if enemy.health > 0:
      print("You attacked the", enemies[current_enemyid]["name"], "for", crit,  "damage!\nHealth:", enemy.health)
    else:
      
      #victory and get item
      
      print("You attacked the", enemies[current_enemyid]["name"], "for", crit,  "damage!")
      enemy_chosen = False

      #SET NEW DROP
      current_itemid = random.choice(list(items["regular_items"]))

      #INCREMENT QUANTITY OF NEW DROP IN ITEM DICTIONARY
      items["regular_items"][current_itemid]["item_quantity"] = items["regular_items"][current_itemid]["item_quantity"] + 1
      #IF ITEM IS NOT ACQUIRED YET, SET TO TRUE AND APPEND IT'S ID TO INVENTORY
      if items["regular_items"][current_itemid]["obtaiend"] == False:
        items["regular_items"][current_itemid]["obtaiend"] = True
        inventory.append(current_itemid)

      #result = (str(items["regular_items"][current_itemid]["item_quantity"]), items["regular_items"][current_itemid]["name"])
      #DEFINE A NEW ARRAY CALLED named_inventory
      #USING LIST COMPREHENSION, SET named_inventory TO 
      def get_quantity_and_turn_into_string(id): #krischin did this
        return str(items["regular_items"][id]["item_quantity"]) + " " + items["regular_items"][id]["name"]
        
      named_inventory = [get_quantity_and_turn_into_string(x) for x in inventory]
          
      print("You've defeated the", enemies[current_enemyid]["name"], "!\nYou recieved a", (items["regular_items"][current_itemid]["name"]), "!")
      print(named_inventory)
      get_choice_1()

    #enemy is attacking
    player_computed_defense = (player.defense + items["armor"][current_armorid]["defense"])
    player.health = player.health - (enemy.attack - player_computed_defense)
    #death
      
    if player.health > 0:
      print("The", enemy.attack_name, "\n The", enemies[current_enemyid]["name"], "attacked you for", enemy.attack - (player.defense + items["armor"][current_armorid]["defense"]), "damage!\nYour Health:", player.health)
      break
    else:
      print("The", enemy.attack_name, "\n The", enemies[current_enemyid]["name"], "attacked you for", enemy.attack - (player.defense + items["armor"][current_armorid]["defense"]), "damage!")
      enemy_chosen = False
      dead = True
      return


def choice_defend():
  global enemy_chosen
  global dead
  
  print("You are defending the enemy's attack!")

  #enemy is attacking
  
  player_computed_defense = (player.defense + items["armor"][current_armorid]["defense"] + (player.defense * 2))
  player.health = player.health - (enemy.attack - player_computed_defense)
  
  #death
    
  if player.health > 0:
    print("The", enemy.attack_name, "\n The", enemies[current_enemyid]["name"], "attacked you for", enemy.attack - (player.defense + items["armor"][current_armorid]["defense"]), "damage!\nYour Health:", player.health)
  else:
    print("The", enemy.attack_name, "\n The", enemies[current_enemyid]["name"], "attacked you for", enemy.attack - (player.defense + items["armor"][current_armorid]["defense"]), "damage!")
    enemy_chosen = False
    dead = True
    return
  

def attack_choice():
  global current_enemyid
  global current_itemid
  global enemy_chosen
  global multiple_value_item
  global enemy
  global dead
  while True:
    if enemy_chosen == False:
      current_enemyid = enemy_roll()
      enemy = classroom.enemy_stats(enemies[current_enemyid]["health"], enemies[current_enemyid]["attack"], enemies[current_enemyid]["attack_name"])
      enemy_chosen = True
    if enemy_chosen == True:
      while True:
        answer_2 = input('What do you do?\n1.Attack\n2.Defend.\n3.Run\nAnswer: ')
        if answer_2 == "1" : choice_attack()
        if answer_2 == "2" : choice_defend()
        if answer_2 == "3" : 
          print("You ran away!")
          enemy_chosen = False
          get_choice_1()
        if dead == True:
          return
        else:
          print("What?")

#sats, equipment, and inventory

def check_stats():
  print("Here are your stats:\nHelath: ", player.health, "\nAttack: ", player.attack + items["weapons"][current_weaponid]["attack"], "\nDefense: ", player.defense + items["armor"][current_armorid]["defense"], "\nCurrent Weapon: ", items["weapons"][current_weaponid]["name"], "\nCurrent Armor: ", items["armor"][current_armorid]["name"])

def access_inventory():
  print(inventory)
  
                
                
                
#rolling

def enemy_roll():
  current_enemyid = random.choice(list(enemies))
  print('A', enemies[current_enemyid]["name"], 'appeared!\nHealth:', enemies[current_enemyid]["health"])
  return current_enemyid
  

def roll_for_weapon(dictionary):
  global current_weaponid
  print("Rolling for a weapon")
  current_weaponid = random.choice(list(dictionary))
  print("Your new weapon is a:", dictionary[current_weaponid]["name"],"!")
  get_choice_1()
  
def roll_for_armor(dictionary):
  global current_armorid
  print("Rolling for armor")
  current_armorid = random.choice(list(dictionary))
  print("Your new armor is:", dictionary[current_armorid]["name"],"!")
  get_choice_1()

#things

items = {
  "weapons" : {
    0 : {
      "name" : "Fist",
      "attack" : 1,
    },
    1 : {
      "name" : "Greatsword",
      "attack" : 2,
    },
    2 : {
      "name" : "Hammer",
      "attack" : 3,
    },
    3 : {
      "name" : "Slingshot",
      "attack" : 4
    },
    4 : {
      "name" : "Whip",
      "attack" : 6
    },
    5 : {
      "name" : "Yo-yo",
      "attack" : 9
    },
    6 : {
      "name" : "Gun",
      "attack" : 12
    },
    7 : {
      "name" : "Rock",
      "attack" : 20
    },
  },
  "armor" : {
    8 : {
      "name" : "Leather Armor",
      "defense" : 2,
    },
     9 : {
      "name" : "Iron Armor",
      "defense" : 4,
    },
     10 : {
      "name" : "Plastic Armor",
      "defense" : 7,
    },
     11 : {
      "name" : "Dragon Armor",
      "defense" : 9,
    },
     12 : {
      "name" : "Glass Armor",
      "defense" : 11,
    },
     13 : {
      "name" : "Fursuit Armor",
      "defense" : 15,
    },
     14 : {
      "name" : "Stone Armor",
      "defense" : 30,
    },
  },
  "regular_items" : {
    15 : {
      "name" : "Twig",
      "item_quantity" : 0,
      "obtaiend" : False
    },
    16 : {
      "name" : "Cat",
      "item_quantity" : 0,
      "obtaiend" : False
    },
    17 : {
      "name" : "Plane Ticket",
      "item_quantity" : 0,
      "obtaiend" : False
    },
    18 : {
      "name" : "Pokemon Card",
      "item_quantity" : 0,
      "obtaiend" : False
    },
    19 : {
      "name" : "Headphones",
      "item_quantity" : 0,
      "obtaiend" : False
    },
    20 : {
      "name" : "Water Bottle",
      "item_quantity" : 0,
      "obtaiend" : False
    },
    21 : {
      "name" : "Health Potion",
      "item_quantity" : 0,
      "obtaiend" : False
    },
    22 : {
      "name" : "Cure to Cancer",
      "item_quantity" : 0,
      "obtaiend" : False
    },
    23 : {
      "name" : "Weed",
      "item_quantity" : 0,
      "obtaiend" : False
    },
    24 : {
      "name" : "Genki Textbook",
      "item_quantity" : 0,
      "obtaiend" : False
    },
    25 : {
      "name" : "PC",
      "item_quantity" : 0,
      "obtaiend" : False
    },
    26 : {
      "name" : "Domo Coffee",
      "item_quantity" : 0,
      "obtaiend" : False
    },
    27 : {
      "name" : "Secret Item",
      "item_quantity" : 0,
      "obtaiend" : False
    },
    28 : {
      "name" : "Poop",
      "item_quantity" : 0,
      "obtaiend" : False
    },
  },
}

enemies = {
  1 : {
    "name" : "Slime",
    "health" : 20,
    "attack" : 12,
    "attack_name" : "Slime used swish!",
  },
  2 : {
    "name" : "Skeleton",
    "health" : 30,
    "attack" : 15,
    "attack_name" : "Skeleton used spook!",
  },
  3 : {
    "name" : "Robot",
    "health" : 40,
    "attack" : 18,
    "attack_name" : "Robot used calculate!",
  },
  4 : {
    "name" : "Sea Bear",
    "health" : 70,
    "attack" : 23,
    "attack_name" : "Seabear used bite!",
  },
  5 : {
    "name" : "Monkey",
    "health" : 14,
    "attack" : 43,
    "attack_name" : "Monkey used scream!",
  },
  6 : {
    "name" : "Kid Named Finger",
    "health" : 40,
    "attack" : 36,
    "attack_name" : "Kid Named Finger used his finger!",
  },
  7 : {
    "name" : "Enemy 15",
    "health" : 30,
    "attack" : 40,
    "attack_name" : "Enemy 15 used attack!",
  },
  8 : {
    "name" : "Dark Chao",
    "health" : 12,
    "attack" : 76,
    "attack_name" : "Dark Chao used gun!",
  },
  9 : {
    "name" : "Herobrine",
    "health" : 67,
    "attack" : 61,
    "attack_name" : "Herobrine used remove",
  },
  10 : {
    "name" : "Heavy from Tfort2",
    "health" : 85,
    "attack" : 64,
    "attack_name" : "Heavy from Tfort2 used Sasha",
  },
  11 : {
    "name" : "God",
    "health" : 100,
    "attack" : 70,
    "attack_name" : "God used slap",
  },
}