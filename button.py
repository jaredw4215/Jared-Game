import pygame

class Button:
    def __init__(self, img_path, pos, scale = 1.0):
        self.image = pygame.image.load(img_path).convert_alpha()
        
        orgin_width = self.image.get_width()
        origin_height = self.image.get_height()
        new_width = int(orgin_width * scale)
        new_height = int(origin_height * scale)
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        
        self.rect = self.image.get_rect(center=pos)
    
    def draw(self, window):
        window.blit(self.image, self.rect)
    
    def is_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]
        
        if self.rect.collidepoint(mouse_pos):
            if mouse_pressed:
                return True
        return False