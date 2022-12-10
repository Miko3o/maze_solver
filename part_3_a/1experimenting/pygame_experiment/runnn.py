import pygame
from sys import exit

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

#this is the display surface/game window
screen = pygame.display.set_mode((350, 250))

clock = pygame.time.Clock()

#regular surface
test_surface = pygame.Surface((120,200))
test_surface.fill('Red')

#drawing a shape
pygame.draw.rect(test_surface, white, [100, 100, 10, 10])

while True:
  #event loop checks every type of input
  #pygame.event.get() method gets all the events and the for loop just loops through all of them
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      
      #this is the opposite from pygame.init()
      pygame.quit()
      
      #this method closes any code once you call it
      exit()

  screen.blit(test_surface, (0, 0))
      
  #updates the display surface
  pygame.display.update()
  clock.tick(60)