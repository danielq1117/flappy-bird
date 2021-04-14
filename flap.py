import pygame, sys, random

def crear_tubo():
  altura_random =random.choice(altura_tubo)
  tubo_abajo = superficie_tubo.get_rect(midtop = (350,altura_random))
  tubo_arriba = superficie_tubo.get_rect(midbottom = (350,altura_random - 150))
  return tubo_abajo, tubo_arriba

def mover_tubos(tubos):
  for tubo in tubos:
    tubo.centerx -= 5
  tubos_visibles = [tubo for tubo in tubos if tubo.right > -50]
  return tubos_visibles

def mostrar_tubos(tubos):
  for tubo in tubos:
    if tubo.bottom >= 512:
      pantalla.blit(superficie_tubo,tubo)
    else:
      voltear_tubo = pygame.transform.flip(superficie_tubo,False,True)
      pantalla.blit(voltear_tubo,tubo)

def detectar_colisiones(tubos):
  for tubo in tubos:
    if rect_ave.colliderect(tubo):
      return False

  if rect_ave.top <= -50 or rect_ave.bottom >= 450:
    return False

  return True

pygame.init()
pantalla = pygame.display.set_mode((288,512))
reloj = pygame.time.Clock()

# Variables del Juego
gravedad = 0.25
movimiento_ave = 0
juego_activo = True

superficie_fondo = pygame.image.load('assets/background-day.png').convert()
superficie_suelo = pygame.image.load('assets/base.png').convert()
pos_suelo_x = 0

superficie_ave = pygame.image.load('assets/bluebird-midflap.png').convert()
rect_ave = superficie_ave.get_rect(center = (50,256))

superficie_tubo = pygame.image.load('assets/pipe-green.png').convert()
lista_tubos = []
SPAWNTUBO = pygame.USEREVENT
pygame.time.set_timer(SPAWNTUBO, 1200)
altura_tubo = [200,300,400]

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        if juego_activo:
          movimiento_ave = -7
        else:
          juego_activo = True
          lista_tubos.clear()
          rect_ave.center = (50,256)
          movimiento_ave = 0

    if event.type == SPAWNTUBO:
      lista_tubos.extend(crear_tubo())

  pantalla.blit(superficie_fondo, (0,0))

  if juego_activo:
    # Ave
    movimiento_ave += gravedad
    rect_ave.centery += movimiento_ave
    pantalla.blit(superficie_ave,rect_ave)
    juego_activo = detectar_colisiones(lista_tubos)

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