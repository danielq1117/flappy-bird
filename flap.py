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

def girar_ave(ave):
  nueva_ave = pygame.transform.rotozoom(ave,-movimiento_ave * 3,1)
  return nueva_ave

def animacion_ave():
  nueva_ave = cuadros_ave[index_ave]
  nuevo_rect_ave = nueva_ave.get_rect(center = (50,rect_ave.centery))
  return nueva_ave,nuevo_rect_ave

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

ave_bajo = pygame.image.load('assets/bluebird-downflap.png').convert_alpha()
ave_medio = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
ave_alto = pygame.image.load('assets/bluebird-upflap.png').convert_alpha()
cuadros_ave = [ave_bajo,ave_medio,ave_alto]
index_ave = 0
superficie_ave = cuadros_ave[index_ave]
rect_ave = superficie_ave.get_rect(center = (50,256))

FLAPAVE = pygame.USEREVENT + 1
pygame.time.set_timer(FLAPAVE, 200)

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

    if event.type == FLAPAVE:
      if index_ave < 2:
        index_ave += 1
      else:
        index_ave = 0

      superficie_ave,rect_ave = animacion_ave()

  pantalla.blit(superficie_fondo, (0,0))

  if juego_activo:
    # Ave
    movimiento_ave += gravedad
    rect_ave.centery += movimiento_ave
    ave_girada = girar_ave(superficie_ave)
    pantalla.blit(ave_girada,rect_ave)
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