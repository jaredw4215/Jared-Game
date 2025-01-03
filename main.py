#Author: Jared Winkens

#Imports
import pygame
from pygame.locals import *
import sys

pygame.init()
FPS = 30
FramePerSec = pygame.time.Clock()
info = pygame.display.Info()
screen_width = info.current_w * 0.8
screen_height = info.current_h * 0.8

window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("The Light Child: Prophecy")

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    FramePerSec.tick(FPS)