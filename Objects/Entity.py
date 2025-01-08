import pygame

class Entity(): # Clase general para representar entidades
    def __init__(self, pos: list, size: tuple, sprite):
        self.pos = pos
        self.size = size
        self.sprite = sprite
        self.health = 10
        self.speed = 1
        self.hitbox = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.turned_left = False
        self.frame = 0

    def mover(self, speed: tuple): # Desplaza la entidad y su hitbox
        if self.pos[0] + speed[0] < 1080 - self.size[0]:
            self.pos[0] += speed[0]
        if self.pos[1] + speed[1] < 720 - self.size[1]:
            self.pos[1] += speed[1]
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], self.size[0]-5, self.size[1]-10)
        
    def draw(self, screen): # Representa la entidad en la pantalla
        ''' Descomentar para ver las hitboxes '''
        # pygame.draw.rect(screen, (255, 255, 255), self.hitbox)
        sprite = self.sprite
        if self.turned_left: 
            sprite = pygame.transform.flip(sprite, flip_x=True, flip_y=False)
        screen.blit(sprite, self.pos)

    def is_hitting(self, entity):
        if self.hitbox.colliderect(entity.hitbox):
            entity.health -= 1 

    def track(self, entity): # Hace que la entidad se aproxime a otra entidad
        if entity.pos[0] > self.pos[0]:
            self.mover((self.speed, 0))
            self.turned_left = True
        if entity.pos[0] < self.pos[0]: 
            self.mover((-self.speed, 0))
            self.turned_left = False
        if entity.pos[1] > self.pos[1]: 
            self.mover((0, self.speed))
        if entity.pos[1] < self.pos[1]: 
            self.mover((0, -self.speed))
        self.is_hitting(entity)