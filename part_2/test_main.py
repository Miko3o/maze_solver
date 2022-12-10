import pytest
from main import Inventory

class TestSuiteExample:

  #Inventory Adds Items to it's inventory
  def test_addsItems(self):
    #Setup
    inventory = Inventory([])

    #Do Work
    inventory.AddItem("thing")

    #Assert
    assert len(inventory.inventory) == 1

    #Tear Down
    #Stuff

  #Inventory Removes Items from it's inventory
  def test_removesItems(self):
    #Setup
    inventory = Inventory(["thing"])

    #Do Work
    inventory.RemoveItem("thing")

    #Assert
    assert len(inventory.inventory) == 0

    #Tear Down

  #Inventory Retrieves the correct item from it's inventory
  def test_getsItems(self):
    #Setup
    inventory = Inventory(["a"])

    #Do Work
    a = inventory.GetItem("a")

    #Assert
    assert a == a

    #Tear Down