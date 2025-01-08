import pygame
from Objects.Entity import Entity

class Soldado(Entity):
    def __init__(self, pos, size):
        super().__init__(pos, size, pygame.image.load('assets/soldier.png'))
        self.health = 99
        self.speed = 3
        self.animation_cooldown = 100
        self.last_time = 0
        self.current_time = 0
        self.is_attacking = False
        self.dash_frames = 0
        self.hitbox = pygame.Rect(pos[0] + 30, pos[1] + 30, size[0] - 40, size[1] - 20)
        self.attack_hitbox = pygame.Rect(pos[0] + 65, pos[1] + 10, size[0] - 30, size[1])

    def attack(self, entities): # Hace que la hitbox de ataque haga daño
        if self.is_attacking:
            for entity in entities:
                if self.attack_hitbox.colliderect(entity.hitbox):
                    entity.health -= 10

    def mover(self, speed): # Ajuste del metodo de entidad para que tambien desplace la hitbox de ataque
        if self.pos[0] + speed[0] < 1080 - self.size[0] and self.pos[0] + speed[0] > 0 - 10:
            self.pos[0] += speed[0]
        if self.pos[1] + speed[1] < 720 - self.size[1] and self.pos[1] + speed[1] > 0 - 30:
            self.pos[1] += speed[1]
        self.hitbox = pygame.Rect(self.pos[0] + 30, self.pos[1] + 30, self.size[0] - 40, self.size[1] - 20)
        if self.turned_left:
            self.attack_hitbox = pygame.Rect(self.pos[0], self.pos[1] + 10, self.size[0] - 30, self.size[1])
        else:
            self.attack_hitbox = pygame.Rect(self.pos[0] + 65, self.pos[1] + 10, self.size[0] - 30, self.size[1])

    def dash(self):
        if self.dash_frames == 0:
            self.dash_frames = 5

        if self.dash_frames > 0:
            self.speed *= 3

    
    def draw(self, screen):  # Ajuste del metodo de entidad para que tambien represente la hitbox de ataque
        ''' Descomentar para ver las hitboxes '''
        # pygame.draw.rect(screen, (255, 255, 255), self.hitbox)
        # if self.is_attacking:
        #     pygame.draw.rect(screen, (0, 255, 0), self.attack_hitbox)
        # else:
        #     pygame.draw.rect(screen, (255, 0, 0), self.attack_hitbox)
        sprite = self.sprite
        if self.turned_left: 
            sprite = pygame.transform.flip(sprite, flip_x=True, flip_y=False)
        screen.blit(sprite, self.pos)

    def update_animation(self): # Cambia el frame del soldado segun el estado de la animacion (pendiente de refinar)
        if self.is_attacking:
            self.current_time += 20
            if self.current_time >= self.animation_cooldown:
                self.current_time = 0
                if self.is_attacking: self.frame += 1
            sheet = pygame.image.load('assets/heavy_attack.png').convert_alpha()
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
                self.sprite = pygame.image.load('assets/soldier.png').convert_alpha()
                surface = self.sprite

            surface.set_colorkey((0,0,0))
            self.sprite = surface