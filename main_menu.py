import pygame
from pygame.locals import *
import sys
from button import Button
from text import Text

class MainMenu:
    def __init__(self, window):
        self.window = window
        
        self.title_pos = (int(window.get_width() * 0.5), int(window.get_height() * 0.1))
        self.title = Text("The Light Child: Prophecy",'Showcard Gothic',self.title_pos,80,(255,0,0))
                
        self.start_button_pos = (int(window.get_width() * 0.5), int(window.get_height() * 0.4))
        self.quit_button_pos = (int(window.get_width() * 0.5), int(window.get_height() * 0.8))
        
        self.start_button = Button("__assets__/button/temp_start_button.png",self.start_button_pos,15)
        self.quit_button = Button("__assets__/button/temp_quit_button.png",self.quit_button_pos,15)
    
    def show(self):
        self.window.fill((245,245,220))
        
        self.title.draw(self.window)
        self.start_button.draw(self.window)
        self.quit_button.draw(self.window)


    
    