import pygame
from pygame.locals import *
from enum import Enum

pos_vec = pygame.math.Vector2
SPEED = 15

class State(Enum):
    IDLE = 0
    WALKING = 1
    
class Person (pygame.sprite.Sprite):
    
    def __init__(self, walk_images, idle_images, pos): 
        super().__init__()
        
        self.state = State.IDLE
        self.frame = 0
        self.orientation = 0
        self.animation_speed = 1/12
        self.cnt = 0
        self.pos = pos_vec(pos)
        
        self.idle_images = idle_images        
        self.walk_images = walk_images
        
        self.image = self.idle_images[self.orientation][self.frame]
        self.rect = self.image.get_rect(center=pos)
        #self.surf = pygame.Surface((50,50))
        #self.surf.fill((128,255,40))
        #self.rect = self.surf.get_rect(center=pos)
        
    
    def move(self, window):
        
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[K_LEFT]:
            self.pos.x -= SPEED
            self.state = State.WALKING
            self.orientation = 1
        if pressed_keys[K_RIGHT]:
            self.pos.x += SPEED
            self.state = State.WALKING
            self.orientation = 2
        if pressed_keys[K_UP]:
            self.pos.y -= SPEED
            self.state = State.WALKING
            self.orientation = 3
        if pressed_keys[K_DOWN]:
            self.pos.y += SPEED
            self.state = State.WALKING
            self.orientation = 0
        if not (pressed_keys[K_DOWN] or pressed_keys[K_UP] or pressed_keys[K_LEFT] or pressed_keys[K_RIGHT]):
            self.state = State.IDLE

        if self.pos.x > window.get_width():
            self.pos.x = window.get_width()
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.y > window.get_height():
            self.pos.y = window.get_height()
        if self.pos.y < 0:
            self.pos.y = 0
        
        if self.state == State.IDLE:
            self.animate(self.idle_images)
        if self.state == State.WALKING:
            self.animate(self.walk_images)
        self.rect.center = self.pos
    
    def animate(self, images):
        self.cnt += (self.animation_speed + (SPEED / 100))
        self.frame = round(self.cnt) % len(images[self.orientation])
        self.image = images[self.orientation][self.frame]
          
    def draw(self, window):
        window.blit(self.image, self.rect)