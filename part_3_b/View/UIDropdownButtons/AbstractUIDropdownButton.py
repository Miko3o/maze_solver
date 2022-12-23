import pygame
from View.GameStateENUM import GameState as gs, ButtonType as bt

class AbstractUIDropdownButton():

  def __init__(self, gameWindow, buttonColor, buttonText, buttonWidth, buttonHeight, displayX, displayY, viewManager):

    #button properties
    self.gameWindow = gameWindow
    self.buttonColor = buttonColor
    self.buttonText = buttonText
    self.buttonWidth = buttonWidth
    self.buttonHeight = buttonHeight
    self.displayX = displayX
    self.displayY = displayY

    #View Manager
    self.viewManager = viewManager

    #rectangle
    self.rect = pygame.draw.rect(self.gameWindow, (self.buttonColor), [self.displayX, self.displayY, self.buttonWidth, self.buttonHeight])
    self.r = False
    self.g = False
    self.b = False

    #text
    self.textfont = pygame.font.SysFont("verdana", 15)
    self.displayText = self.textfont.render(self.buttonText, 1, (0, 0, 0))
    self.text_rect = self.displayText.get_rect(center=(self.displayX + (self.buttonWidth/2), self.displayY + (self.buttonHeight/2)))


    #clicking
    self.clicked = False
    self.mouseHover = False

  
  def Draw(self, mouseX, mouseY):
    #button
    color = tuple(self.buttonColor)
    self.rect = pygame.draw.rect(self.gameWindow, (color), [self.displayX, self.displayY, self.buttonWidth, self.buttonHeight])
    
    topLeft = (self.displayX, self.displayY)
    bottomLeft = (self.displayX, self.displayY + self.buttonHeight)
    bottomRight = (self.displayX + self.buttonWidth, self.displayY + self.buttonHeight)
    topRight = (self.displayX + self.buttonWidth, self.displayY)
    
    pygame.draw.lines(self.gameWindow, (0, 0, 0), True, [topLeft, bottomLeft, bottomRight, topRight], 4)

    

    #hover mouse over button

    if self.rect.collidepoint(mouseX, mouseY) == True and self.mouseHover == False:
      if self.buttonColor[0] < 205:
        self.buttonColor[0] += 50
        self.r = True
      if self.buttonColor[1] < 205:
        self.buttonColor[1] += 11
        self.g = True
      if self.buttonColor[2] < 205:
        self.buttonColor[2] += 30
        self.b = True
      self.mouseHover = True
    elif self.rect.collidepoint(mouseX, mouseY) == False and self.mouseHover == True:
      if self.r == True:
        self.buttonColor[0] -= 50
        self.r = False
      if self.g == True:
        self.buttonColor[1] -= 11
        self.g = False
      if self.b == True:
        self.buttonColor[2] -= 30
        self.b = False
      self.mouseHover = False

    #text
    self.gameWindow.blit(self.displayText, self.text_rect)
    
    

  def ClickButton(self, mouseX, mouseY):
    #button on click
    if self.rect.collidepoint(mouseX, mouseY) == True:
      if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        self.clicked = True
        self.rect = pygame.draw.rect(self.gameWindow, (100, 100, 100), [self.displayX, self.displayY, self.buttonWidth, self.buttonHeight])
        print("clicked")

  
  def UnclickButton(self, mouseX, mouseY, buttonType):
    #button off click
    if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True and buttonType == bt.SELECT_OBJECT:
      print("unclicked")
      self.clicked = False
      return gs.SELECTING_GRID_OBJECT
    elif pygame.mouse.get_pressed()[0] == 0 and self.clicked == True and buttonType == bt.PICK_SOLVE_ALG:
      print("unclicked")
      self.clicked = False
      return gs.PICKING_SOLVING_ALG
    elif pygame.mouse.get_pressed()[0] == 0 and self.clicked == True and buttonType == bt.PICK_SORT_ALG:
      print("unclicked")
      self.clicked = False
      return gs.PICKING_SORTING_ALG
    else:
      return gs.CREATING_MAZE