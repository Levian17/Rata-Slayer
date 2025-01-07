import pygame

class Entity():
    def __init__(self, pos: list, size: tuple, sprite):
        self.pos = pos
        self.size = size
        self.sprite = sprite
        self.hitbox = pygame.Rect(pos[0] + 30, pos[1] + 30, size[0] - 40, size[1] - 20)
        self.turned_left = False
        self.is_attacking = False
        self.frame = 0

    def mover(self, speed: tuple):
        self.pos[0] += speed[0]
        self.pos[1] += speed[1]
        self.hitbox = pygame.Rect(self.pos[0] + 30, self.pos[1] + 30, self.size[0] - 40, self.size[1] - 20)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.hitbox)
        sprite = self.sprite
        if self.turned_left: 
            sprite = pygame.transform.flip(sprite, flip_x=True, flip_y=False)
        screen.blit(sprite, self.pos)
        


class Soldado(Entity):
    def __init__(self, pos, size):
        super().__init__(pos, size, pygame.image.load('soldier.png'))
        self.animation_cooldown = 80
        self.last_time = 0
        self.current_time = 0

    def update_animation(self):
        if self.is_attacking:
            self.current_time += 20
            if self.current_time >= self.animation_cooldown:
                self.current_time = 0
                if self.is_attacking: self.frame += 1
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
                self.sprite = pygame.image.load('soldier.png')
                surface = self.sprite
            self.sprite = surface