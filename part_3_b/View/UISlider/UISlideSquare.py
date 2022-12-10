import pygame
from View.GameStateENUM import GameState as gs

class UISlideSquare():

  def __init__(self, background):

    #button properties
    self.background = background
    self.buttonColor = (255, 255, 255)
    self.buttonOutlineColor = (0, 0, 0)
    self.buttonText = "Grid Size"
    self.buttonWidth = 30
    self.buttonHeight = 30
    self.displayX = 507
    self.displayY = 285

    #rectagnle
    self.rect = pygame.draw.rect(self.background, (self.buttonColor), [self.displayX, self.displayY, self.buttonWidth, self.buttonHeight])
    
    #text
    self.textfont = pygame.font.SysFont("verdana", 20)
    self.displayText = self.textfont.render(self.buttonText, 1, (0, 0, 0))
    self.text_rect = self.displayText.get_rect(center=(self.displayX + (self.buttonWidth/2), self.displayY - 20))

    
    #clicking
    self.clicked = False
    self.offsetX = 0
    
  
  def Draw(self, mouseX, mouseY):
    #button
    self.rect = pygame.draw.rect(self.background, (self.buttonColor), [self.displayX, self.displayY, self.buttonWidth, self.buttonHeight])
    pygame.draw.lines(self.background, self.buttonOutlineColor, True, [(self.displayX, self.displayY), (self.displayX, self.displayY + self.buttonHeight), (self.displayX + self.buttonWidth, self.displayY + self.buttonHeight), (self.displayX + self.buttonWidth, self.displayY)], 4)

    #text
    self.background.blit(self.displayText, self.text_rect)

    

  def ClickButton(self, mouseX, mouseY): 
    #button on click
    if self.rect.collidepoint(mouseX, mouseY):
      if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        self.clicked = True
        self.rect = pygame.draw.rect(self.background, (100, 100, 100), [self.displayX, self.displayY, self.buttonWidth, self.buttonHeight])
        self.offsetX = self.displayX - mouseX
        print("clicked")

  def UnclickButton(self, mouseX, mouseY):
    #button off click
    if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
      print("unclicked")
      self.clicked = False
      return gs.CREATING_MAZE
      
  def DragSquare(self, mouseX, mouseY):
    if self.clicked and self.displayX > 463 and self.displayX < 556:
      self.displayX = mouseX + self.offsetX
    #collision
    if self.displayX < 464:
      self.displayX = 464
    if self.displayX > 555:
      self.displayX = 555
    return self.displayX