import pygame, sys, random

pygame.init()
pantalla = pygame.display.set_mode((288,512))
reloj = pygame.time.Clock()

superficie_fondo = pygame.image.load('assets/background-day.png').convert()
superficie_suelo = pygame.image.load('assets/base.png').convert()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  pantalla.blit(superficie_fondo, (0,0))

  pantalla.blit(superficie_suelo,(0,450))
  
  pygame.display.update()
  reloj.tick(60)