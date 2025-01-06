import pygame
import os

class SpriteSheetLoader:
    def __init__(self):
        self.matrix = [[],[],[],[]]
    
    # returns a 2D matrix of images where each row represents the sprite's orientation 
    # and each col represents a frame in that orientation
    def load(self, images_path, images_size):
        for image in os.listdir(images_path + "front"):
            self.matrix[0].append(pygame.transform.scale((pygame.image.load(f'{images_path + "front"}/{image}').convert_alpha()), images_size))
        for image in os.listdir(images_path + "left"):
            self.matrix[1].append(pygame.transform.scale((pygame.image.load(f'{images_path + "left"}/{image}').convert_alpha()), images_size))
        for image in os.listdir(images_path + "right"):
            self.matrix[2].append(pygame.transform.scale((pygame.image.load(f'{images_path + "right"}/{image}').convert_alpha()), images_size))
        for image in os.listdir(images_path + "back"):
            self.matrix[3].append(pygame.transform.scale((pygame.image.load(f'{images_path + "back"}/{image}').convert_alpha()), images_size))
        return self.matrix