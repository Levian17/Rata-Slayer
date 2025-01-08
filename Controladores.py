import pygame
from pygame import K_w, K_a, K_s, K_d, K_SPACE, KEYDOWN, K_RIGHT, K_LEFT
from random import choice, randint
from Objects.Entity import Entity
from Sound import play_sound

# Genera las ratas
def entity_spawn(entities, soldier, dificultad):
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

# Elimina las ratas
def entity_despawn(entities):
    for entity in entities: # Eliminamos las entidades que estan muertas
        if entity.health <= 0: 
            play_sound('flesh')
            entities.remove(entity)

# Controla los inputs del teclado (key_pressed y key_down)
def keys_controller(pressed_keys, events, soldier):
    # Pressed keys
    if pressed_keys[K_s]:
        soldier.mover((0, soldier.speed))
    if pressed_keys[K_w]:
        soldier.mover((0, -soldier.speed))
    if pressed_keys[K_a]:
        if soldier.frame == 0: soldier.turned_left = True
        soldier.mover((-soldier.speed, 0))
    if pressed_keys[K_d]:
        if soldier.frame == 0: soldier.turned_left = False
        soldier.mover((soldier.speed, 0))
    if pressed_keys[K_SPACE]:
        soldier.dash()

    # Key downs
    for event in events:
        if event.type == KEYDOWN: # Controlador KEYDOWN    
            if event.key == K_RIGHT or event.key == K_LEFT: # Arrows
                if soldier.frame == 0: 
                    soldier.attack_hitbox = pygame.Rect(soldier.pos[0] + 65, soldier.pos[1] + 10, soldier.size[0] - 30, soldier.size[1])
                    soldier.is_attacking = True
                    play_sound('slash')

                    if event.key == K_LEFT:
                        soldier.turned_left = True
                    elif event.key == K_RIGHT:
                        soldier.turned_left = False