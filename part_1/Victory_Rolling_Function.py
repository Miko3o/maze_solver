from Dictionaries_for_Items_and_Enemies import items
from Item import Item
import random

def roll_for_item(player, enemy, item, gameState, enemy_chosen):
  #you just won an enemy drop
  itemID = random.choice(list(items["regular_items"]))
  item = Item(items["regular_items"][itemID]["name"])
  item_pair = (1, item.name)
  print("You've defeated the", enemy.name, "!\nYou recieved a", item.name, "!\n")  
  item_in_inventory = False
  
  for item_exist in Item.Inventory:
    if item_exist[1] == item_pair[1]:
      item_in_inventory = True
      new_item_exist = (item_exist[0] + 1, item_exist[1])
      Item.Inventory.remove(item_exist)
      Item.Inventory.append(new_item_exist)
      break
  if item_in_inventory == False:
    Item.Inventory.append(item_pair)
  
  return