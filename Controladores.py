import pygame
from pygame import K_w, K_a, K_s, K_d, K_SPACE
from random import choice, randint
from Entity import Entity

def enemy_generation(entities, soldier, dificultad):
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
    
def keys_controller(pressed_keys, soldier):
    if pressed_keys[K_s]:
        soldier.mover((0, soldier.speed))
    if pressed_keys[K_w]:
        soldier.mover((0, -soldier.speed))
    if pressed_keys[K_a]:
        soldier.turned_left = True
        soldier.mover((-soldier.speed, 0))
    if pressed_keys[K_d]:
        soldier.turned_left = False
        soldier.mover((soldier.speed, 0))
    if pressed_keys[K_SPACE]:
        soldier.dash()