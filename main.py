import sys
import pygame
from Entity import Soldado
from pygame.locals import KEYDOWN, K_ESCAPE, K_w, K_a, K_s, K_d, K_RIGHT, K_LEFT

# Settings basicos de pygame
pygame.display.set_caption('Slasher Game')
screen = pygame.display.set_mode((1080, 720))
running: bool = True
clock = pygame.time.Clock()

# Inicializamos una entidad soldado y lo representamos en la pantalla.
soldier = Soldado([50, 50], (96, 96))

while running: # Ciclo de juego
    for event in pygame.event.get(): # Controlador de eventos
        if event.type == pygame.QUIT: # Boton X
            running = False            
        if event.type == KEYDOWN: # Controlador KEYDOWN
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_RIGHT:
                soldier.turned_left = False
                soldier.is_attacking = True
            if event.key == K_LEFT:
                soldier.turned_left = True
                soldier.is_attacking = True

    # Controlador movimiento
    pressed_keys = pygame.key.get_pressed()    
    if pressed_keys[K_s]:
        soldier.mover((0, 5))
    if pressed_keys[K_w]:
        soldier.mover((0, -5))
    if pressed_keys[K_a]:
        soldier.turned_left = True
        soldier.mover((-5, 0))
    if pressed_keys[K_d]:
        soldier.turned_left = False
        soldier.mover((5, 0))

    # Controlador ataque
    soldier.update_animation()

    # Controlador de la pantalla
    screen.fill((0, 0, 0))
    soldier.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()