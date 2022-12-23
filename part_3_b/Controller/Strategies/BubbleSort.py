from Controller.Strategies.AbstractStrategy import AbstractStrategy
from View.GameStateENUM import GridObjects as go
import pygame

class BubbleSort(AbstractStrategy):

  def __init__(self, *args):
    super().__init__(*args)

  def Sort(self, currentGrid):
    print("wip")