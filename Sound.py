import pygame

pygame.mixer.init()

slash = pygame.mixer.Sound("assets/slash.mp3")
slash.set_volume(0.2)

flesh = pygame.mixer.Sound("assets/flesh.mp3")
flesh.set_volume(0.35)

def play_sound(sound: str):
    if sound == 'slash':
        pygame.mixer.Sound.play(slash)
    if sound == 'flesh':
        pygame.mixer.Sound.play(flesh)