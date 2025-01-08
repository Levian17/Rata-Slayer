import sys
import pygame
import time
from Entity import Soldado
from Controladores import enemy_generation, keys_controller
from pygame.locals import KEYDOWN, K_ESCAPE, K_RIGHT, K_LEFT

# Settings core de pygame
screen = pygame.display.set_mode((1080, 720))
running: bool = True
clock = pygame.time.Clock()
pygame.font.init()
pygame.mixer.init()

# Settings opcionales
pygame.display.set_caption('Slasher Game')
font = pygame.font.SysFont('Arial', 40,)
slash = pygame.mixer.Sound("assets/slash.mp3")
flesh = pygame.mixer.Sound("assets/flesh.mp3")
slash.set_volume(0.2)
flesh.set_volume(0.35)

# Variables de logica
contador_ratas = 0
dificultad = 0

# Generacion de entidades
soldier = Soldado([300, 300], (96, 96))
entities = []

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
                pygame.mixer.Sound.play(slash)
            if event.key == K_LEFT: # Arrow izquierdasa
                soldier.turned_left = True
                soldier.attack_hitbox = pygame.Rect(soldier.pos[0], soldier.pos[1] + 10, soldier.size[0] - 30, soldier.size[1])
                soldier.is_attacking = True
                pygame.mixer.Sound.play(slash)

    for entity in entities: # Eliminamos las entidades que estan muertas
        if entity.health <= 0: 
            pygame.mixer.Sound.play(flesh)
            entities.remove(entity)

    # Generacion de entidades
    if enemy_generation(entities, soldier, dificultad):
        contador_ratas += 1
        if contador_ratas % 10 == 0 and dificultad < 40: dificultad += 5
    
    # Controlador movimiento (Mover a funcion ?)
    keys_controller(pygame.key.get_pressed(), soldier)

    # Controlador animaciones
    soldier.update_animation()

    # Controlador ataque
    soldier.attack(entities)

    # Refrescar pantalla
    screen.fill((30, 30, 30))

    # Representar vida
    pygame.draw.rect(screen, (220, 165, 75), (50, 150-soldier.health, 90, soldier.health))
    screen.blit(font.render(str(soldier.health), False, (255, 255, 255)), (75, 75))
    screen.blit(pygame.image.load("assets/engranaje.png"), (20, 20), (0, 0, 148, 156))

    # Representar soldado
    soldier.draw(screen)

    # Movimiento y representacion entidades
    for entity in entities:
        entity.track(soldier)
        entity.draw(screen)

    # Hacer que avance un frame
    clock.tick(60)

    # Acabar el ciclo de juego si el jugador no tiene vida
    if soldier.health <= 0: 
        running = False
        screen.fill((30, 30, 30))

    # Mostrar pantalla actualizada
    pygame.display.flip()

# Mensaje de fin de partida
if soldier.health <= 0:
    screen.blit(font.render('Fin de la partida...', False, (255, 255, 255)), (400, 300))
    screen.blit(font.render(f'Ratas eliminadas:  {contador_ratas}', False, (255, 255, 255)), (370, 375))
    pygame.display.flip()
    time.sleep(5)

# Finalizar la ejecucion
pygame.quit()
sys.exit()