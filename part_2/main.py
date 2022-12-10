class Inventory:

  def __init__(self, items):
    self.inventory = items

  def AddItem(self, item):
    self.inventory.append(item)

  def RemoveItem(self, item):
    self.inventory.remove(item)

  def GetItem(self, desiredItem):
    for item in self.inventory:
      if item == desiredItem:
        return desiredItem
    return None
