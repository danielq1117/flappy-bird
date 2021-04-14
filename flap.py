import pygame, sys, random

def crear_tubo():
  tubo_nuevo = superficie_tubo.get_rect(midtop = (350,256))
  return tubo_nuevo

def mover_tubos(tubos):
  for tubo in tubos:
    tubo.centerx -= 5
  return tubos

def mostrar_tubos(tubos):
  for tubo in tubos:
    pantalla.blit(superficie_tubo,tubo)

pygame.init()
pantalla = pygame.display.set_mode((288,512))
reloj = pygame.time.Clock()

# Variables del Juego
gravedad = 0.25
movimiento_ave = 0

superficie_fondo = pygame.image.load('assets/background-day.png').convert()
superficie_suelo = pygame.image.load('assets/base.png').convert()
pos_suelo_x = 0

superficie_ave = pygame.image.load('assets/bluebird-midflap.png').convert()
rect_ave = superficie_ave.get_rect(center = (50,256))

superficie_tubo = pygame.image.load('assets/pipe-green.png').convert()
lista_tubos = []
SPAWNTUBO = pygame.USEREVENT
pygame.time.set_timer(SPAWNTUBO, 1200)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        movimiento_ave = -7
    if event.type == SPAWNTUBO:
      lista_tubos.append(crear_tubo())

  pantalla.blit(superficie_fondo, (0,0))

  # Ave
  movimiento_ave += gravedad
  rect_ave.centery += movimiento_ave
  pantalla.blit(superficie_ave,rect_ave)

  # Tubos
  lista_tubos = mover_tubos(lista_tubos)
  mostrar_tubos(lista_tubos)
  
  # Suelo
  pos_suelo_x -= 1
  pantalla.blit(superficie_suelo,(pos_suelo_x,450))
  pantalla.blit(superficie_suelo,(pos_suelo_x + 288,450))
  if pos_suelo_x <= -288:
    pos_suelo_x = 0
  
  pygame.display.update()
  reloj.tick(60)