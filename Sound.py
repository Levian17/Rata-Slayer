import pygame

pygame.mixer.init()

# Sounds
slash = pygame.mixer.Sound("assets/slash.mp3")
slash.set_volume(0.2)
flesh = pygame.mixer.Sound("assets/flesh.mp3")
flesh.set_volume(0.35)

# Songs
electro = pygame.mixer.music.load("assets/electro.mp3")
battle = pygame.mixer.music.load("assets/battle.mp3")

def play_sound(sound: str):
    if sound == 'slash':
        pygame.mixer.Sound.play(slash)
    if sound == 'flesh':
        pygame.mixer.Sound.play(flesh)

def play_music(song: str):
    if song == "electro":
        pygame.mixer.music.play(electro)
    if song == "battle":
        pygame.mixer.music.play(battle)