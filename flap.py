import pygame, sys, random

pygame.init()
pantalla = pygame.display.set_mode((288,512))
reloj = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  pygame.display.update()
  reloj.tick(60)