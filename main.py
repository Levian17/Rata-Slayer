import sys
import pygame
from random import randint
from Entity import Entity, Soldado
from pygame.locals import KEYDOWN, K_ESCAPE, K_w, K_a, K_s, K_d, K_RIGHT, K_LEFT

# Settings basicos de pygame
pygame.display.set_caption('Slasher Game')
screen = pygame.display.set_mode((1080, 720))
running: bool = True
clock = pygame.time.Clock()

# Generacion de entidades
soldier = Soldado([50, 50], (96, 96))
entities = []
def enemy_generation(entities):
    if randint(0, 100) == 0:
        entities.append(Entity([randint(100, 900), randint(100, 600)], (96, 96), pygame.image.load('assets/soldier.png')))

while running: # Ciclo de juego

    for event in pygame.event.get(): # Controlador de eventos
        if event.type == pygame.QUIT: # Boton X
            running = False            
        if event.type == KEYDOWN: # Controlador KEYDOWN
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_RIGHT: # Arrow derecha
                soldier.turned_left = False
                soldier.attack_hitbox = pygame.Rect(soldier.pos[0] + 65, soldier.pos[1] + 10, soldier.size[0] - 30, soldier.size[1])
                soldier.is_attacking = True
            if event.key == K_LEFT: # Arrow izquierda
                soldier.turned_left = True
                soldier.attack_hitbox = pygame.Rect(soldier.pos[0], soldier.pos[1] + 10, soldier.size[0] - 30, soldier.size[1])
                soldier.is_attacking = True

    # Generacion de entidades
    enemy_generation(entities)

    # Controlador movimiento (Mover a funcion ?)
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

    # Controlador animaciones
    soldier.update_animation()

    # Controlador ataque
    soldier.attack(entities)

    # Refrescar pantalla
    screen.fill((0, 0, 0))
    # Representar soldado
    soldier.draw(screen)
    # Movimiento y representacion entidades
    for entity in entities: 
        entity.track(soldier)
        entity.draw(screen)

    # Mostrar pantalla actualizada
    pygame.display.flip()
    # Hacer que avance un frame
    clock.tick(60)

# Finalizar la ejecucion
pygame.quit()
sys.exit()