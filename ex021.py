import pygame
pygame.mixer.init()
pygame.mixer.music.load('begin.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
