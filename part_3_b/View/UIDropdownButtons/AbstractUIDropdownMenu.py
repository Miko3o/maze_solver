import pygame
from View.GameStateENUM import GridObjects as go

class AbstractUIDropdownMenu():

  def __init__(self, gameWindow, menuText, menuReturn, menuWidth, menuHeight, displayX, displayY):

    #menu properties
    self.gameWindow = gameWindow
    self.menuColor = (255, 255, 255)
    self.menuText = menuText
    self.menuReturn = menuReturn
    self.menuWidth = menuWidth
    self.menuHeight = menuHeight
    self.displayX = displayX
    self.displayY = displayY


    #rectangle
    self.menuSelect = []

    #text
    
    self.textfont = pygame.font.SysFont("verdana", 17)

    #clicking
    self.clicked = False
    self.mouseHover = False

    #grid object
    self.gridObject = go.WALL


  def Draw(self, mouseX, mouseY):
    #menu
    previousTextHeight = 0
    previousTextSpacing = 0
    options = []
    textRectWidth = []
    textRectHeight = []
    for text, ret in zip(self.menuText, self.menuReturn):
      optionsText = self.textfont.render(text, 1, (0, 0, 0))
        
      #rectangle
      optionsRect = pygame.draw.rect(self.gameWindow, (self.menuColor), [self.displayX, self.displayY + previousTextHeight + previousTextSpacing + 5, self.menuWidth, 17])
      

      #hover mouse over selection
      if optionsRect.collidepoint(mouseX, mouseY) == True and self.mouseHover == False:
        self.menuColor = (222, 243, 255)
        self.mouseHover = True
      elif optionsRect.collidepoint(mouseX, mouseY) == False and self.mouseHover == True:
        self.menuColor = (255, 255, 255)
        self.mouseHover = False

      #clicking
      if optionsRect.collidepoint(mouseX, mouseY) == True:
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
          self.clicked = True
          optionsRect = pygame.draw.rect(self.gameWindow, (100, 100, 100), [self.displayX, self.displayY + previousTextHeight + previousTextSpacing + 5, self.menuWidth, self.menuHeight])
          self.gridObject = ret
          print("menu selection clicked")

        
      #redrawing rectangle for mouse over color
      optionsRect = pygame.draw.rect(self.gameWindow, (self.menuColor), [self.displayX, self.displayY + previousTextHeight + previousTextSpacing + 5, self.menuWidth, 17])
      
      #text
      self.gameWindow.blit(optionsText, (self.displayX + 5, self.displayY + previousTextHeight + + previousTextSpacing + 5))
         
      previousTextHeight += 15
      previousTextSpacing += 4

      



      
    #outline
    topLeft = (self.displayX, self.displayY)
    bottomLeft = (self.displayX, self.displayY + self.menuHeight + previousTextHeight)
    bottomRight = (self.displayX + self.menuWidth, self.displayY + self.menuHeight + previousTextHeight)
    topRight = (self.displayX + self.menuWidth, self.displayY)
    
    pygame.draw.lines(self.gameWindow, (0, 0, 0), True, [topLeft, bottomLeft, bottomRight, topRight], 4)



  
  def ClickOption(self, mouseX, mouseY): 
    print("ClickOption: Unused")

  def UnclickOption(self, mouseX, mouseY):
    #button off click
    if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
      print("Grid Object:", self.gridObject)
      self.clicked = False
      return self.gridObject
    else:
      return self.gridObject