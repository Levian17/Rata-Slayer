import sys
import pygame
import time
from Objects.Soldado import Soldado
from Controladores import entity_spawn, entity_despawn, keys_controller
from Sound import play_music
from pygame.locals import KEYDOWN, K_ESCAPE

# Settings core de pygame
screen = pygame.display.set_mode((1080, 720))
running: bool = True
clock = pygame.time.Clock()
pygame.font.init()

# Settings opcionales
pygame.display.set_caption('Slasher Game')
font = pygame.font.SysFont('Arial', 40,)

# Variables de logica
contador_ratas = 0
dificultad = 0

# Generacion de entidades
soldier = Soldado([300, 300], (96, 96))
entities = []

while running: # Ciclo de juego
    events = pygame.event.get()
    for event in events: # Controladores de salida 
        if event.type == pygame.QUIT: # Boton X
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE: # Tecla ESC
            running = False 
        
    # Despawneamos las entidades muertas
    entity_despawn(entities)
    
    # Spawneamos nuevas entidades
    if entity_spawn(entities, soldier, dificultad):
        contador_ratas += 1
        if contador_ratas % 10 == 0 and dificultad < 40: dificultad += 5
    
    # Controlador movimiento
    keys_controller(pygame.key.get_pressed(), events, soldier)

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