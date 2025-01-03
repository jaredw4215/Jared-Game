import pygame

class Text:
    def __init__(self, desc, font, pos, size, color):
        self.font = pygame.font.SysFont(font,size)
        self.image = self.font.render(desc,True,color)
        self.rect = self.image.get_rect(center=pos)
        
        
    def draw(self, window):
        window.blit(self.image, self.rect)