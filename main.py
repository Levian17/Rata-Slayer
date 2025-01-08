import sys
import pygame
from random import randint, choice
from Entity import Entity, Soldado
from pygame.locals import KEYDOWN, K_ESCAPE, K_w, K_a, K_s, K_d, K_RIGHT, K_LEFT

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
def enemy_generation(entities, soldier):
    if randint(0, 50 - dificultad) == 0:
        pos = [0, 0]
        try:
            if soldier.pos[0] >= 100:
                if choice([True, False]):
                    pos[0] = randint(0, soldier.pos[0] - 100)
                    if pos[0] < 0: pos[0] = 10
                else:
                    pos[0] = randint(soldier.pos[0] + 100, 1000)
                    if pos[0] > 1000: pos[0] = 1000
            else:
                raise Exception

            if soldier.pos[1] <= 1000: 
                if choice([True, False]):
                    pos[1] = randint(0, soldier.pos[1] - 100)
                    if pos[1] < 0: pos[1] = 10
                else:
                    pos[1] = randint(soldier.pos[1] + 100, 600)
                    if pos[1] > 1000: pos[1] = 1000
            else:
                raise Exception

            entities.append(Entity( pos, (80, 80), pygame.image.load('assets/rata.png')))
            return True
        except Exception as e:
            entities.append(Entity([randint(200, 900), randint(100, 600)], (80, 80), pygame.image.load('assets/rata.png')))
            return True
    else:
        return False


while running: # Ciclo de juego

    if soldier.health <= 0: running = False

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

    for entity in entities: # Eliminamos las entidades que estan muertas
        if entity.health <= 0: entities.remove(entity)

    # Generacion de entidades
    if enemy_generation(entities, soldier):
        contador_ratas += 1
        if contador_ratas % 10 == 0 and dificultad < 45: dificultad += 5
        print(dificultad, contador_ratas)
    
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

    # Controlador animacionwes
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

    # Mostrar pantalla actualizada
    pygame.display.flip()
    # Hacer que avance un frame
    clock.tick(60)

# Finalizar la ejecucion
pygame.quit()
sys.exit()