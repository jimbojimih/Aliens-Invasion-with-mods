import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self):
        super().__init__()
        '''initialization of remaining lives image'''
        self.image = pygame.image.load('images/shipBlack2.bmp')
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect() 

    
    
        
    
