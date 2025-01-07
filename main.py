import sys
import pygame
import time
from pygame.locals import KEYDOWN, K_ESCAPE, K_w, K_a, K_s, K_d, K_RIGHT, K_LEFT

# Settings basicos de pygame
pygame.display.set_caption('Slasher Game')
screen = pygame.display.set_mode((1080, 720))
running: bool = True
clock = pygame.time.Clock()

animation_cooldown = 100
last_time = 0
current_time = 0

class Entity(): # Clase entidad, posee una posicion, un tamaño y un sprite.
    def __init__(self, pos: list, size: tuple, sprite):
        self.pos = pos
        self.size = size
        self.sprite = sprite
        self.turned_left = False
        self.sprite
        self.is_attacking = False
        self.frame = 0

    def mover(self, speed: tuple):
        self.pos[0] += speed[0]
        self.pos[1] += speed[1]

    def heavy_attack(self):
        sheet = pygame.image.load('heavy_attack.png')
        surface = pygame.Surface((120, 120))
        if self.frame == 0:
            surface.blit(sheet, (0,0), (self.frame * 120, 0, 120, 120))
        elif self.frame == 1:
            surface.blit(sheet, (0,0), (self.frame * 120, 0, 120, 120))
        elif self.frame == 2:
            surface.blit(sheet, (0,0), (self.frame * 120, 0, 120, 120))
        elif self.frame == 3:
            surface.blit(sheet, (0,0), (self.frame * 120, 0, 120, 120))
        elif self.frame == 4:
            self.frame = 0
            self.is_attacking = False
            soldier.sprite = pygame.image.load('soldier.png')
            surface = self.sprite
        
        self.sprite = surface

    def draw(self):
        sprite = self.sprite
        if self.turned_left: 
            sprite = pygame.transform.flip(sprite, flip_x=True, flip_y=False)
        screen.blit(sprite, self.pos)

# Inicializamos una entidad soldado y lo representamos en la pantalla.
soldier = Entity([50, 50], (96, 96), pygame.image.load('soldier.png'))
soldier.sprite.set_clip()
screen.blit(soldier.sprite, soldier.pos)

while running: # Ciclo de juego
    current_time += 20
    if current_time >= animation_cooldown:
        current_time = 0
        if soldier.is_attacking: soldier.frame += 1

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

    # Controlador de las teclas
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
    if soldier.is_attacking:
        soldier.heavy_attack()

    # Controlador de la pantalla
    screen.fill((0, 0, 0))
    soldier.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()