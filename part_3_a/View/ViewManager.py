import Controller.ControllerManager
import Model.ModelManager

from View.UIGrid import UIGrid
from View.UIButtons.AbstractUIButton import AbstractUIButton
from View.UIButtons.UIGravityButton import UIGravityButton
from View.UIButtons.UILoadButton import UILoadButton
from View.UIButtons.UIRedoButton import UIRedoButton
from View.UIButtons.UISaveButton import UISaveButton
from View.UIButtons.UISolveSortButton import UISolveSortButton
from View.UIButtons.UIUndoButton import UIUndoButton

class ViewManager():
  def __init__(self, background):
    self.controllerManager = Controller.ControllerManager.ControllerManager
    self.modelManager = Model.ModelManager.ModelManager
    
    self.uiGrid = UIGrid()
    self.abstractUIButton = AbstractUIButton(self)
    self.uiGravityButton = UIGravityButton(self)
    self.uiLoadButton = UILoadButton(self, background, "Blue", "hi", 50, 20, 10, 30)
    print("hi")
    self.uiRedoButton = UIRedoButton(self)
    self.uiSaveButton = UISaveButton(self)
    self.uiSolveSortButton = UISolveSortButton(self)
    self.uiUndoButton = UIUndoButton(self)